#!/usr/bin/env python3
"""
CLI скрипт для создания/обновления статьи в KB YouTrack на основе Markdown документа.
Структура документа:
  docs/<doc_name>/
    config.json     # конфигурация: токен, url, project_id, summary, article_id, parent_id
    content.md      # Markdown контент
    attachments/    # файлы для загрузки (необязательно)
"""

import os
import sys
import json
import argparse
from pathlib import Path
import requests
from shutil import copytree
from dotenv import load_dotenv
import re
from urllib.parse import urlparse


def load_global_config():
    # 1. .env
    env_path = Path('.env')
    if env_path.exists():
        load_dotenv(dotenv_path=env_path)
    # 2. ytkb.config.json
    global_cfg = {}
    global_cfg_path = Path('ytkb.config.json')
    if global_cfg_path.exists():
        with open(global_cfg_path, encoding='utf-8') as f:
            global_cfg = json.load(f)
    return {
        'token': os.getenv('YT_TOKEN') or global_cfg.get('token', ''),
        'base_url': os.getenv('YT_BASE_URL') or global_cfg.get('base_url', ''),
        'project_id': os.getenv('PROJECT_ID') or global_cfg.get('project_id', ''),
        'parent_id': os.getenv('PARENT_ID') or global_cfg.get('parent_id', '')
    }


def load_config(path):
    with open(path, encoding='utf-8') as f:
        return json.load(f)


def save_config(path, config):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(config, f, ensure_ascii=False, indent=2)


def merge_config(doc_cfg):
    global_cfg = load_global_config()
    merged = {
        'summary': doc_cfg.get('summary', ''),
        'article_id': doc_cfg.get('article_id', ''),
        'parent_id': doc_cfg.get('parent_id', global_cfg['parent_id']),
        'token': global_cfg['token'],
        'base_url': global_cfg['base_url'],
        'project_id': global_cfg['project_id']
    }
    return merged


def publish_document(doc_path):
    doc_path = Path(doc_path)
    config_path = doc_path / 'config.json'
    content_path = doc_path / 'content.md'
    attachments_dir = doc_path / 'attachments'
    if not config_path.exists():
        print(f"Ошибка: не найден файл конфигурации {config_path}")
        sys.exit(1)
    if not content_path.exists():
        print(f"Ошибка: не найден файл контента {content_path}")
        sys.exit(1)
    doc_cfg = load_config(config_path)
    cfg = merge_config(doc_cfg)
    token = cfg['token']
    base_url = cfg['base_url']
    project_id = cfg['project_id']
    summary = cfg['summary']
    article_id = cfg.get('article_id')
    parent_id = cfg.get('parent_id')
    print(f"DEBUG: parent_id для публикации: {parent_id}")
    if not all([token, base_url, project_id, summary]):
        print("Ошибка: не указаны обязательные параметры token, base_url, project_id или summary")
        print("Проверьте .env или ytkb.config.json в корне проекта!")
        sys.exit(1)
    with open(content_path, encoding='utf-8') as f:
        content = f.read()
    headers_json = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }
    if article_id:
        print(f"Обновление статьи {article_id}...")
        url = f"{base_url}/api/articles/{article_id}?fields=id,summary,content"
        payload = {'summary': summary, 'content': content}
        response = requests.post(url, headers=headers_json, json=payload)
    else:
        print("Создание новой статьи...")
        url = f"{base_url}/api/articles?fields=id"
        payload = {
            'project': {'id': project_id},
            'summary': summary,
            'content': content
        }
        if parent_id:
            payload['parentArticle'] = {'id': parent_id}
        print("DEBUG payload:", json.dumps(payload, ensure_ascii=False, indent=2))
        response = requests.post(url, headers=headers_json, json=payload)
    try:
        response.raise_for_status()
    except requests.HTTPError as e:
        print("Ошибка при запросе:", e, response.text)
        sys.exit(1)
    data = response.json()
    new_id = data.get('id')
    if not article_id and new_id:
        doc_cfg['article_id'] = new_id
        save_config(config_path, doc_cfg)
        article_id = new_id
        print(f"Создана статья с id {article_id}")
    else:
        print(f"Статья обновлена, id {article_id}")
    if attachments_dir.exists() and attachments_dir.is_dir():
        print("Загружаем вложения и собираем URL...")
        # Получить список уже загруженных вложений (по имени)
        uploaded_names = set()
        for file_path in attachments_dir.iterdir():
            if file_path.name == '.gitkeep':
                continue
            if file_path.is_file():
                uploaded_names.add(file_path.name)
        
        # Не загружать повторно файлы с тем же именем
        for file_path in attachments_dir.iterdir():
            if file_path.name == '.gitkeep':
                continue
            if file_path.is_file():
                name = file_path.name
                if name in uploaded_names:
                    print(f"- {name} уже загружен")
                    continue
                print(f"- {name}...")
                with open(file_path, 'rb') as file_stream:
                    files = {'file': file_stream}
                    # Запрашиваем URL загруженного вложения
                    url_attach = f"{base_url}/api/articles/{article_id}/attachments?fields=id,name,url"
                    resp_attach = requests.post(url_attach, headers={'Authorization': f'Bearer {token}'}, files=files)
                try:
                    resp_attach.raise_for_status()
                    data = resp_attach.json()
                    path_url = data.get('url')
                    if path_url:
                        full_url = base_url.rstrip('/') + path_url
                        print(f"{name} загружен успешно")
                    else:
                        print(f"{name} не загружен, так как уже существует")
                except Exception as e:
                    print(f"Ошибка при загрузке {name}: {e} {resp_attach.text}")
        # Если есть загруженные вложения, обновляем ссылки в статье
        if uploaded_names:
            try:
                # Читаем локальный content.md
                with open(content_path, 'r', encoding='utf-8') as f:
                    content_local = f.read()
                # Заменяем локальные пути на URL
                for name in uploaded_names:
                    pattern = r'(!\[[^\]]*\]\()attachments/' + re.escape(name) + r'(\))'
                    content_local = re.sub(pattern, r'\1' + name + r'\2', content_local)
                # Обновляем статью на сервере
                print("Обновляю ссылки на вложения в статье...")
                update_url = f"{base_url}/api/articles/{article_id}?fields=id,summary,content"
                payload_update = {'summary': summary, 'content': content_local}
                resp_update = requests.post(update_url, headers=headers_json, json=payload_update)
                resp_update.raise_for_status()
                print("Ссылки на вложения обновлены")
                # Сохраняем обновлённый content.md локально
                with open(content_path, 'w', encoding='utf-8') as f:
                    f.write(content_local)
            except Exception as e:
                print(f"Ошибка при обновлении ссылок на вложения: {e}")
    else:
        print("Вложений нет или папка 'attachments' отсутствует.")
    print("Готово.")


def import_document(article_id_or_url, doc_name):
    # Определяем article_id: если передан URL, извлекаем slug после 'articles'
    article_id = article_id_or_url
    if article_id_or_url.startswith('http://') or article_id_or_url.startswith('https://'):
        parsed = urlparse(article_id_or_url)
        parts = [seg for seg in parsed.path.split('/') if seg]
        if 'articles' in parts:
            idx = parts.index('articles')
            if idx + 1 < len(parts):
                article_id = parts[idx + 1]
        # else оставляем исходное значение
    # Загрузка конфигурации
    global_cfg = load_global_config()
    token = global_cfg['token']
    base_url = global_cfg['base_url']
    
    if not all([token, base_url, article_id]):
        print("Ошибка: не указаны обязательные параметры token, base_url или article_id")
        print("Проверьте .env или ytkb.config.json в корне проекта!")
        sys.exit(1)
    
    # Создание директории для документа
    workspace_dir = Path('workspace')
    if not workspace_dir.exists():
        workspace_dir.mkdir(parents=True)
    
    doc_path = workspace_dir / doc_name
    if doc_path.exists():
        print(f"Ошибка: папка {doc_path} уже существует")
        sys.exit(1)
    
    doc_path.mkdir(parents=True)
    (doc_path / 'attachments').mkdir()
    
    # Получение данных статьи из YouTrack
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }
    
    url = f"{base_url}/api/articles/{article_id}?fields=id,summary,content,parentArticle(id)"
    print(f"Получение статьи с ID {article_id}...")
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except requests.HTTPError as e:
        print(f"Ошибка при запросе: {e}")
        print(response.text)
        sys.exit(1)
    
    article_data = response.json()
    
    # Сохранение конфигурации
    config = {
        'article_id': article_id,
        'summary': article_data.get('summary', ''),
    }
    
    # Добавление parent_id, если есть
    parent = article_data.get('parentArticle')
    if parent and 'id' in parent:
        config['parent_id'] = parent['id']
    
    config_path = doc_path / 'config.json'
    save_config(config_path, config)
    
    # Сохранение содержимого
    content = article_data.get('content', '')
    content_path = doc_path / 'content.md'
    with open(content_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    # Загрузка вложений
    print("Загрузка вложений...")
    attachments_url = f"{base_url}/api/articles/{article_id}/attachments?fields=id,name,url"
    try:
        att_response = requests.get(attachments_url, headers=headers)
        att_response.raise_for_status()
        attachments = att_response.json()
        
        for attachment in attachments:
            name = attachment.get('name')
            url_path = attachment.get('url')
            # Пропускаем, если нет имени или URL
            if not name or not url_path:
                continue
            print(f"Загрузка вложения: {name}")
            download_url = base_url.rstrip('/') + url_path
            download_resp = requests.get(download_url, headers={'Authorization': f'Bearer {token}'})
            if download_resp.status_code == 200:
                with open(doc_path / 'attachments' / name, 'wb') as f:
                    f.write(download_resp.content)
            else:
                print(f"Ошибка при загрузке вложения {name}: {download_resp.status_code}")
        # Обновление ссылок на вложения в content.md
        try:
            text = ''
            with open(content_path, 'r', encoding='utf-8') as f:
                text = f.read()
            for attachment in attachments:
                name = attachment.get('name')
                if name:
                    text = re.sub(r'(!\[[^\]]*\]\()' + re.escape(name) + r'(\))', r'\1attachments/' + name + r'\2', text)
            with open(content_path, 'w', encoding='utf-8') as f:
                f.write(text)
        except Exception as e:
            print(f"Ошибка при обновлении ссылок на вложения: {e}")
    except Exception as e:
        print(f"Ошибка при загрузке вложений: {e}")
    
    print(f"Документ успешно импортирован в {doc_path}")
    print(f"Теперь вы можете редактировать его и опубликовать изменения с помощью:")
    print(f"python3 cli.py publish \"{doc_name}\"")


def sync_document(doc_name):
    # Синхронизировать локальный документ с YouTrack по article_id в config.json
    workspace_dir = Path('workspace')
    doc_path = workspace_dir / doc_name
    if not doc_path.exists():
        print(f"Ошибка: папка {doc_path} не найдена")
        sys.exit(1)
    config_path = doc_path / 'config.json'
    if not config_path.exists():
        print(f"Ошибка: не найден файл конфигурации {config_path}")
        sys.exit(1)
    doc_cfg = load_config(config_path)
    article_id = doc_cfg.get('article_id')
    if not article_id:
        print("Ошибка: в config.json не указан article_id")
        sys.exit(1)
    # Получаем глобальную конфигурацию
    global_cfg = load_global_config()
    token = global_cfg['token']
    base_url = global_cfg['base_url']
    # Получение данных статьи
    headers = {'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'}
    url = f"{base_url}/api/articles/{article_id}?fields=content"
    try:
        resp = requests.get(url, headers=headers)
        resp.raise_for_status()
    except Exception as e:
        print(f"Ошибка при получении статьи: {e}")
        sys.exit(1)
    content = resp.json().get('content', '')
    # Обновляем content.md
    content_path = doc_path / 'content.md'
    with open(content_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Обновлён файл {content_path}")
    # Синхронизируем вложения
    attachments_dir = doc_path / 'attachments'
    # Очищаем старые вложения
    for file in attachments_dir.iterdir():
        if file.is_file(): file.unlink()
    # Загружаем новые вложения
    att_list_url = f"{base_url}/api/articles/{article_id}/attachments?fields=id,name,url"
    try:
        list_resp = requests.get(att_list_url, headers=headers)
        list_resp.raise_for_status()
        attachments = list_resp.json()
        for att in attachments:
            name = att.get('name')
            url_path = att.get('url')
            # Пропускаем вложения без имени или URL
            if not name or not url_path:
                continue
            dl_url = base_url.rstrip('/') + url_path
            file_resp = requests.get(dl_url, headers={'Authorization': f'Bearer {token}'})
            if file_resp.status_code == 200:
                with open(attachments_dir / name, 'wb') as out:
                    out.write(file_resp.content)
                print(f"Загружено вложение: {name}")
        # Обновление ссылок на вложения в content.md
        try:
            text = ''
            with open(content_path, 'r', encoding='utf-8') as f:
                text = f.read()
            for attachment in attachments:
                name = attachment.get('name')
                if name:
                    text = re.sub(r'(!\[[^\]]*\]\()' + re.escape(name) + r'(\))', r'\1attachments/' + name + r'\2', text)
            with open(content_path, 'w', encoding='utf-8') as f:
                f.write(text)
        except Exception as e:
            print(f"Ошибка при обновлении ссылок на вложения: {e}")
    except Exception as e:
        print(f"Ошибка при загрузке вложений: {e}")
    print("Синхронизация завершена.")


def main():
    parser = argparse.ArgumentParser(description='Утилита для работы с YouTrack KB документами')
    subparsers = parser.add_subparsers(dest='command', required=True)
    # Init
    init_parser = subparsers.add_parser('init', help='Инициализировать новый документ из шаблона')
    init_parser.add_argument('template', help='Имя шаблона в папке templates/')
    init_parser.add_argument('doc', help='Имя рабочей папки в workspace/')
    # Publish
    pub_parser = subparsers.add_parser('publish', help='Публиковать/обновлять документ в YouTrack KB')
    pub_parser.add_argument('doc', help='Имя рабочей папки в workspace/')
    # New BFT
    newbft_parser = subparsers.add_parser('new-bft', help='Создать и сразу опубликовать новый документ БФТ')
    newbft_parser.add_argument('name', help='Название документа (без [Драфт] БФТ)')
    # Import
    import_parser = subparsers.add_parser('import', help='Импортировать существующий документ из YouTrack по ID или URL')
    import_parser.add_argument('article_id', help='ID или URL статьи в YouTrack')
    import_parser.add_argument('doc', help='Имя рабочей папки в workspace/')
    # Sync
    sync_parser = subparsers.add_parser('sync', help='Обновить локальный документ по изменениям в YouTrack')
    sync_parser.add_argument('doc', help='Имя рабочей папки в workspace/')

    args = parser.parse_args()
    if args.command == 'init':
        src = Path('templates') / args.template
        workspace_dir = Path('workspace')
        dst = workspace_dir / args.doc
        if dst.exists():
            print(f"Папка {dst} уже существует")
            sys.exit(1)
        if not workspace_dir.exists():
            workspace_dir.mkdir(parents=True)
        print(f"Копирование шаблона {src} → {dst}")
        copytree(src, dst)
        # Заполнение config.json только уникальными полями
        cfg_path = dst / 'config.json'
        try:
            cfg = load_config(cfg_path)
        except Exception:
            cfg = {}
        save_config(cfg_path, cfg)
        print(f"Инициализация завершена, заполнен config.json")
    elif args.command == 'publish':
        doc_arg = str(Path('workspace') / args.doc)
        publish_document(doc_arg)
    elif args.command == 'new-bft':
        doc_name = f"[Драфт] БФТ {args.name}"
        src = Path('templates') / 'bft'
        workspace_dir = Path('workspace')
        dst = workspace_dir / doc_name
        # Создаем папку и копируем шаблон, если она еще не существует
        if not workspace_dir.exists():
            workspace_dir.mkdir(parents=True)

        if not dst.exists():
            print(f"Копирование шаблона {src} → {dst}")
            copytree(src, dst)
            # Заполнить config.json только уникальными полями
            cfg_path = dst / 'config.json'
            try:
                cfg = load_config(cfg_path)
            except Exception:
                cfg = {}
            cfg['summary'] = doc_name
            save_config(cfg_path, cfg)
        else:
            print(f"Папка {dst} уже существует, пропускаю создание шаблона")

        # Публикуем документ (новый или существующий)
        print("Публикация документа в YouTrack...")
        publish_document(dst)
        print(f"Документ создан и опубликован: {doc_name}")
    elif args.command == 'import':
        import_document(args.article_id, args.doc)
    elif args.command == 'sync':
        sync_document(args.doc)


if __name__ == '__main__':
    main() 