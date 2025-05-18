# Модели данных RCT24

## Основные сущности

### User

```json
{
  "id": "uuid",
  "email": "string",
  "firstName": "string",
  "lastName": "string",
  "role": "enum(USER, ADMIN)",
  "status": "enum(ACTIVE, BLOCKED)",
  "createdAt": "datetime",
  "updatedAt": "datetime"
}
```

### Order

```json
{
  "id": "uuid",
  "userId": "uuid",
  "status": "enum(NEW, PROCESSING, COMPLETED, CANCELLED)",
  "items": [
    {
      "productId": "uuid",
      "quantity": "integer",
      "price": "decimal"
    }
  ],
  "totalAmount": "decimal",
  "createdAt": "datetime",
  "updatedAt": "datetime"
}
```

### Product

```json
{
  "id": "uuid",
  "name": "string",
  "description": "string",
  "price": "decimal",
  "status": "enum(ACTIVE, INACTIVE)",
  "createdAt": "datetime",
  "updatedAt": "datetime"
}
```

## Правила именования

- Используйте camelCase для полей
- UUID для идентификаторов
- Enum для статусов и ролей
- Обязательные поля createdAt и updatedAt
- Мягкое удаление через status

## Связи между сущностями

- User 1:N Order
- Order N:M Product
- Product N:1 Category

## Индексы

- Первичные ключи: id
- Внешние ключи: userId, productId
- Составные индексы: (userId, status)
