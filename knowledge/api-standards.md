# API Стандарты RedCat

## REST API (Laravel)

### Организация маршрутов

- Все маршруты описаны в `routes/api.php` внутри группы:

```php
Route::prefix('v1')
     ->middleware('auth:api')
     ->namespace('Api\V1')
     ->group(function () {
         Route::apiResource('users', 'UserController');
         // ... другие ресурсы
     });
```

- Используйте `Route::apiResource()` для CRUD-эндпоинтов
- Наименования маршрутов (`->name()`): `users.index`, `users.show`, `users.store`, `users.update`, `users.destroy`

### Именование контроллеров и методов

- Контроллеры располагаются в `App\Http\Controllers\Api\V1`
- Название контроллера в единственном числе с суффиксом `Controller`, например `UserController`
- Методы: `index`, `show`, `store`, `update`, `destroy`

### Именование эндпоинтов

- Пути в нижнем регистре во множественном числе:
  - `/api/v1/users`
  - `/api/v1/users/{id}`
- Вложенные ресурсы через `/`, например `/api/v1/users/{id}/orders`

### HTTP Methods

- GET — получение данных (`index`, `show`)
- POST — создание (`store`)
- PUT — полное обновление (`update`)
- PATCH — частичное обновление (`update`)
- DELETE — удаление (`destroy`)

### Коды ответов

- 200 OK — успешное получение или изменение ресурса
- 201 Created — успешное создание ресурса
- 204 No Content — успешное удаление или обновление без тела
- 400 Bad Request — неверные параметры запроса
- 401 Unauthorized — не аутентифицирован
- 403 Forbidden — нет прав доступа
- 404 Not Found — ресурс не найден
- 422 Unprocessable Entity — ошибка валидации (FormRequest)
- 500 Internal Server Error — внутренняя ошибка сервера

### Валидация запросов

- Используйте FormRequest классы в `App\Http\Requests` для валидации входных данных
- При ошибках валидации автоматически возвращаются:

```json
HTTP/1.1 422 Unprocessable Entity
{
  "message": "The given data was invalid.",
  "errors": {
    "field_name": [
      "Ошибка 1",
      "Ошибка 2"
    ]
  }
}
```

### Формат ответа

#### Одиночный ресурс

Используйте Laravel API Resource классы (`App\Http\Resources`):

```php
return new UserResource($user);
```

Пример JSON:

```json
{
  "data": {
    "id": "uuid",
    "name": "John Doe"
    // ... другие поля
  }
}
```

#### Коллекция ресурсов

Используйте Resource Collection:

```php
return UserResource::collection($users);
```

Пример JSON с пагинацией:

```json
{
  "data": [
    {
      /* элемент 1 */
    },
    {
      /* элемент 2 */
    }
  ],
  "meta": {
    "current_page": 1,
    "per_page": 20,
    "total": 100
  }
}
```

## Event-Driven API (Laravel Broadcasting)

- Используйте события в `App\Events`
- Для broadcast-событий реализуйте интерфейс `ShouldBroadcast`
- Определяйте каналы в `routes/channels.php`, например:
  ```php
  Broadcast::channel('user.{id}', function ($user, $id) {
      return (int) $user->id === (int) $id;
  });
  ```
- Шаблон имени события — класс события: `App\Events\UserCreated`
- Формат сообщения для broadcast:

```json
{
  "event": "App\\Events\\UserCreated",
  "data": {
    "id": "uuid",
    "name": "John Doe"
  }
}
```

### Прием real-time уведомлений

- На фронтенде используйте Laravel Echo или Pusher
- Подписывайтесь на канал:
  ```js
  Echo.private(`user.${userId}`).listen("UserCreated", (e) => {
    /* обработка */
  });
  ```
