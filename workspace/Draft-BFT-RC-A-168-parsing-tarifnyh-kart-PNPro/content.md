| Номер задачи Epic |  |
| --- | --- |
| Номер задачи БФТ |  |
| К какому сроку? | к X дате |
| В какой релиз целимся? | 3.0 |
| Необходимо предварительно реализовать БФТ | \- |

(Product)

## **Проблематика:**

В системе используется множество тарифных карт, которые часто меняются. Вручную актуализировать эти карты сложно и трудозатратно. Поставщики, у которых есть свои API или сайты, публикуют актуальные данные о тарифах, которые можно парсить и автоматически загружать в систему. Требуется внедрение механизма автоматического парсинга и загрузки тарифных карт, чтобы сократить время на обновление данных и снизить вероятность ошибок.

## **Цель:**

Создать автоматизированную систему парсинга и загрузки тарифных карт поставщиков в систему тарифов, разработанную на Strapi v4, с возможностью предварительного хранения, обогащения и нормализации данных перед их использованием в системе. Автоматически отправлять тарифные карты на API Gateway для дальнейшей передачи в Bitrix24 и на сайт.

## **Польза для бизнеса:**

- Снижение нагрузки на сотрудников, которые вручную обновляют тарифные карты.
- Быстрая актуализация тарифных данных, что увеличивает точность расчетов и уменьшает риск ошибок.
- Повышение эффективности управления тарифами и улучшение качества данных.

## **Польза для юзера:**

- Гарантия работы с актуальными тарифами.
- Снижение ошибок и времени ожидания при обновлении данных в системе.
- Автоматизированные уведомления об изменениях тарифов и возможностях их доработки.

## **Метрики:**

### Какие сейчас метрики:
- Среднее время на обновление тарифной карты: X часов.
- Количество ошибок, связанных с устаревшими данными: Y.

### Какие метрики должны измениться и на сколько:
- Снижение среднего времени на обновление тарифной карты на 70%.
- Снижение числа ошибок, связанных с устаревшими данными, на 90%.

### Excel файл, модель метрик с прогнозом изменения:
- Вложить Excel-файл с подробным прогнозом и моделированием улучшения метрик.

## **Термины и сокращения (Product)**

| Термин, сокращение | Определение, расшифровка |
| --- | --- |
| Система тарифов | Модуль для хранения и управления тарифными картами, разработанный на Strapi v4. |
| Парсинг | Процесс автоматического сбора данных с внешних источников (API или веб-страниц). |
| Тарифная карта | Документ или набор данных, описывающий тарифы поставщика. |

## **Background (Product)**

Референсы, конкуренты, исследования, запросы бизнеса:
- Анализ конкурентных решений по автоматизации управления тарифами.
- Запросы от отдела финансов на улучшение оперативности обновления тарифных данных.
- Обзор аналогичных решений по автоматизации парсинга и нормализации данных.

## **Затрагиваемые платформы: (BA) - (Атыя / Владимир)**

| Платформа | Затронуто? |
| --- | --- |
| Сайт фронтенд | Нет |
| Сайт бэкенд | Нет |
| Битрикс | Нет |
| API Gateway | Да |
| Интеграция | Да |
| Парсер | Да |
| Система тарифов | Да |

## **AS-IS \| TO BE (Product)**

| Как сейчас | Как должно быть |
| --- | --- |
| Тарифные карты обновляются вручную, сотрудники проверяют данные и загружают их в систему тарифов | Автоматический парсинг данных тарифов у поставщиков, нормализация и сохранение данных в системе тарифов с минимальным ручным участием |

## **Пользовательские требования на сайте: (Product)**

| Требование | Описание |
| --- | --- |
| Отображение актуальных тарифных карт | Пользователи должны видеть актуальные данные по тарифам на сайте. |
| Уведомления об изменениях тарифов | При изменении тарифов ответственный сотрудник должен получать уведомление для ручной доработки карты. |

## **Список User Stories: (Product)**

| **Модуль** | **Название** | **US \ JTBD** | **Критерии приемки** | **Релиз** |
| --- | --- | --- | --- | --- |
| Парсер тарифов | Автоматическое обновление тарифных карт | Как сотрудник, я хочу, чтобы система автоматически обновляла тарифные карты из API или сайта поставщика, чтобы всегда работать с актуальными данными | Тарифные карты обновляются автоматически, данные корректно отображаются в системе тарифов | 3.0 |
| Нормализация тарифов | Обогащение данных тарифных карт | Как администратор системы, я хочу, чтобы загруженные тарифные карты автоматически нормализовались и обогащались справочниками перед использованием | Данные тарифа обогащены необходимыми справочниками и подготовлены для работы в системе | 3.0 |

## **Дизайн-макеты: (Design)**

(Дизайн интерфейсов не требуется, так как данные обрабатываются на уровне backend и API.)

## **Элементы интерфейса: (Product)**

Картинка с цифрами над каждым элементом и таблица описания каждого элемента. (Не требуется.)

## **Обязательные поля, валидация и сортировка: (Product)**

### **Поля формы и их валидация**

| Поле | Тип данных | Обязательное? | Валидация | Предварительные состояния |
| --- | --- | --- | --- | --- |
| Источник данных | Справочник | Да | Проверка доступности источника | Задается при настройке парсинга |
| UUID тарифной карты | Строка | Да | Уникальный идентификатор карты | Генерируется автоматически |

### **Поля таблицы и сортировка**

| Поле | Тип данных | Сортировка? |
| --- | --- | --- |
| Дата обновления | Дата | Да |
| Источник | Строка | Нет |

## **Требования к аналитике данных: (Product)**

- Отслеживать количество обновленных тарифных карт.
- Количество ошибок при обновлении тарифов.
- Среднее время до появления тарифной карты в активном статусе после парсинга.

## **Функциональные требования: (ФТ) - US для разработки (Владимир)**

### **1\. User Story:** Парсинг и загрузка тарифных карт в систему

**Описание**: Как администратор системы, я хочу, чтобы новые тарифные карты автоматически собирались с сайтов поставщиков или через их API, обогащались справочниками и попадали в систему тарифов.

### **Frontend**

(Фронтенд не требуется)

### **Backend**

1. Модуль парсинга данных должен извлекать только нужные параметры из источников данных (сайт или API поставщика).
2. Сохранять извлеченные данные тарифной карты во временное хранилище для последующего обогащения.
3. Обогащать данные тарифов справочниками и нормализовать данные перед их загрузкой в систему тарифов.
4. При наличии старой тарифной карты система должна обновлять дату окончания этой карты и сохранять новую версию.
5. Загруженные карты попадают в систему тарифов в статусе "Выключено" для последующей ручной доработки.

### **Критерии приемки:**

* **Backend**:
  1. Данные собираются автоматически из источников данных и сохраняются во временное хранилище.
  2. Обогащение данными справочников происходит автоматически перед загрузкой в систему тарифов.
  3. Тарифные карты загружаются в систему тарифов в статусе "Выключено".

**Пример/Кейс:**

* **Кейс**: Источник данных поставщика обновляет тарифные карты.
* **Действие**: Система автоматически парсит новые данные и сохраняет их в систему тарифов.
* **Результат**: Новая тарифная карта появляется в системе в статусе "Выключено".

### **2\. User Story:** Уведомление о загрузке новой тарифной карты

**Описание**: Как администратор системы, я хочу получать уведомления в Телеграм о загруженных тарифных картах для ручной доработки и активации.

### **Frontend**

(Фронтенд не требуется)

### **Backend**

1. Реализовать интеграцию с Телеграм для отправки уведомлений о новых тарифных картах ответственному сотруднику.
2. После загрузки новой тарифной карты в систему тарифов отправлять уведомление с деталями карты и ссылкой для её доработки.

### **Критерии приемки:**

* **Backend**:
  1. После каждой загрузки новой тарифной карты в статусе "Выключено" отправляется уведомление в Телеграм ответственному сотруднику.

**Пример/Кейс:**

* **Кейс**: Новая тарифная карта успешно загружена в систему тарифов.
* **Действие**: Система отправляет уведомление ответственному сотруднику в Телеграм.
* **Результат**: Сотрудник получает уведомление и проводит доработку карты.

## **Схема взаимодействия между системами: (BA)**

### Описание взаимодействия:
1. **Поставщики**: Поставщики обновляют тарифные карты на своих веб-сайтах или через API.
2. **Парсер**:
   - Автоматически собирает данные тарифных карт с сайтов и API поставщиков.
   - Нормализует и обогащает данные справочниками, чтобы унифицировать формат перед загрузкой в систему тарифов.
   - Сохраняет тарифные карты в статусе "Выключено" для последующей проверки и доработки.
3. **API Gateway**:
   - Обеспечивает интеграцию между парсером и системой тарифов.
   - Передает данные тарифных карт из парсера в модуль тарифов на сайте и в другие системы.
4. **Система тарифов**:
   - Получает данные от парсера через API Gateway.
   - Хранит тарифные карты в структуре данных с полями для даты обновления, источника данных и уникального идентификатора (UUID).
   - Обеспечивает интерфейс для ручной доработки и активации загруженных тарифов ответственным сотрудником.
5. **Телеграм-бот**:
   - Получает уведомления о новых тарифных картах, загруженных в систему тарифов.
   - Отправляет ответственным сотрудникам уведомления о необходимости доработки и активации тарифной карты.

### Шаги:
1. **Сбор данных**:
   - Парсер автоматически собирает данные о тарифных картах с сайтов и API поставщиков.
2. **Обработка и нормализация данных**:
   - Система нормализует данные и обогащает их необходимыми справочниками.
3. **Сохранение во временное хранилище**:
   - Нормализованные данные тарифных карт сохраняются для последующего анализа.
4. **Передача в систему тарифов через API Gateway**:
   - Данные тарифных карт передаются в систему тарифов через API Gateway и сохраняются в статусе "Выключено".
5. **Отправка уведомления в Телеграм**:
   - Телеграм-бот отправляет уведомление ответственным сотрудникам о новой тарифной карте, которая требует доработки.
6. **Ручная доработка и активация**:
   - Ответственные сотрудники проверяют и дорабатывают тарифные карты в системе тарифов перед активацией.

### Пример данных и путей передачи
- **Источник данных**: API поставщика или сайт.
- **Парсер**: Собирает данные с внешнего источника и передает через API Gateway.
- **Система тарифов**: Получает данные через API Gateway и сохраняет их с UUID.
- **Телеграм-бот**: Уведомляет ответственного сотрудника о необходимости доработки тарифной карты.

### Зависимости:
1. **Парсер** должен быть настроен для поддержки нескольких источников данных с разными форматами (API, веб-страницы).
2. **API Gateway** должен корректно передавать данные в систему тарифов, сохраняя структуру и формат данных.
3. **Телеграм-бот** должен быть интегрирован с системой уведомлений для своевременного информирования ответственных сотрудников.

### Затрагиваемые системы:
- **Парсер** — для автоматического сбора и нормализации данных.
- **API Gateway** — для интеграции между парсером и системой тарифов.
- **Система тарифов** — для хранения и управления тарифными картами.
- **Телеграм-бот** — для уведомлений сотрудников о новых данных для доработки.