# Проект "Test_Hammer"

Работа над проектом «Тестовое задание для Python разработчика» - реализация простой реферальной системы.

Основные возможности:
- авторизация по номеру телефона
- запрос на профиль пользователя
- возможно реферальной системы(инвайт код)
- сервис Список покупок
- реализация админ панели

## Технический стек:
- [Python 3.9.10](https://docs.python.org/release/3.9.10/)
- [Django 3.2](https://docs.djangoproject.com/en/3.2/)
- [Django REST Framework 3.12.4](https://www.django-rest-framework.org/topics/documenting-your-api/)
- [python-dotenv 1.0.0](https://pypi.org/project/python-dotenv/)
- [PostgreSQL 16](https://www.postgresql.org/docs/16/release-16-2.html)

## Запуск проекта:
[файл примера переменных](./infra-dev/.env.example)

[развёртывание проекта](./SetUp.md)

## Документация API:
```
Документация Swagger UI
http://127.0.0.1:8000/swagger/
```

```
Документация Django Rest Framework
http://127.0.0.1:8000/docs/
```

```
Документация ReDoc
http://127.0.0.1:8000/redoc/
```



## Примеры запроса в Postman:

[коллекция Postman](./Collection_test_Hammer.postman_collection.json)

### 1 Пример:
Запрос кода
```
Метод: POST
http://127.0.0.1:8000/api/send-code/
```
```
{
    "phone_number": "номер телефона"
}
```

### 2 Пример:
Проверка кода
```
Метод: POST
http://127.0.0.1:8000/api/verify-code/
```
```
{
    "phone_number": "номер телефона",
    "code": "4-ех значный код"
}
```

### 3 Пример:
Инвайт код
```
Метод: POST
http://127.0.0.1:8000/api/activate-invite/
```
```
{
    "inviting_code": "инвайт код"
}
```

### 4 Пример:
Получения списка пользователей
```
Метод: GET
http://127.0.0.1:8000/api/invited-users/
```


## Комманда:

[GitHub](https://github.com/TheDoBa) | Разработчик - Vladimir Avizhen
