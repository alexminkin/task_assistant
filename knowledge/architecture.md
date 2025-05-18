# Архитектурные принципы компании

## Общая архитектура

- Микросервисная архитектура
- Event-driven взаимодействие между системами
- REST API для внешних интеграций
- Асинхронная обработка длительных операций
- Постепенное развертывание (Canary, Blue-Green)

## Компоненты системы

- Tariff System (Strapi v4)
- API Gateway (FastAPI + Celery)
- Central Data Store (PostgreSQL)
- Site Database (PostgreSQL)
- Bitrix24 (CRM)
- Website (React + Laravel API)
- ElasticSearch (поисковый движок)
- Monitoring & Logging (Prometheus, Grafana, Loki)

## Схема взаимодействия

- Frontend и Site Backend взаимодействуют через Laravel API
- Все интеграции с Bitrix24 проходят через API Gateway
- Tariff System отправляет изменения тарифных карт через API Gateway

```mermaid
flowchart LR
    subgraph Strapi["Tariff System (Strapi v4)"]
        TS[Tariff Service]
    end
    subgraph AG["API Gateway (FastAPI + Celery)"]
        GW[Gateway]
        Q[Celery Queue]
        DBc[(Central PostgreSQL)]
    end
    subgraph Laravel["Site Backend (Laravel API)"]
        LAR[LaravelAPI]
        SDB[(Site PostgreSQL DB)]
    end
    subgraph FE["Frontend (React)"]
        FEApp[React App]
    end
    subgraph B24["Bitrix24 (CRM)"]
        CRM
    end

    %% Тарифные карты
    TS -->|Create/Update Tariff| GW
    GW -->|Validate & Save| DBc
    GW -->|Push Tariff to B24| CRM
    GW -->|Push Tariff to Site| LAR

    %% Основное взаимодействие Frontend <-> Site Backend
    FEApp -->|API Request| LAR
    LAR -->|Read/Write Data| SDB
    LAR -->|Response| FEApp

    %% Интеграция Site <-> B24 через Gateway
    LAR -->|Call B24| GW
    GW -->|Forward to B24| CRM
    CRM -->|Event via Gateway| GW
    GW -->|Forward Event to Site| LAR

    %% Поисковый запрос
    LAR -->|Search Query| ES[ElasticSearch]
    ES -->|Search Results| LAR
```

## Основные сценарии

1. **Работа с тарифами:**

   - Strapi сохраняет тарифную карту → API Gateway валидирует и сохраняет в центральную БД → Gateway трансформирует и отсылает данные в Bitrix24 и на сайт через Laravel API

2. **Поисковый фильтр:**
   - React фронтенд отправляет фильтрационный запрос → Laravel API обогащает и формирует запрос к ElasticSearch → ES возвращает результаты → Laravel API обогащает и отдает фронтенду

## API Gateway (FastAPI + Celery)

- FastAPI для синхронных REST эндпоинтов `/v1/tariff-cards`, `/v1/sync/*`
- Celery для фоновых задач (валидация, маппинг, отправка)
- Конфигурация маппинга сервисов, авторизаций и маршрутов хранится в PostgreSQL

## Безопасность

- Аутентификация сервисов через JWT/OAuth2
- HTTPS для всех коммуникаций

## Масштабируемость и отказоустойчивость

- Горизонтальное масштабирование сервисов
- Кластеризация PostgreSQL с репликацией
- Мониторинг SLA и алёрты через Prometheus и Grafana
