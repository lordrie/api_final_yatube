# API для Yatube

## Описание
Это API для приложения Yatube, которое предоставляет доступ к своим данным по определенному URL.
API включает в себя возможность получения, создания, редактирования и удаления публикаций, а также работы с группами и комментариями.

* Удобство использования: API предоставляет простой и понятный интерфейс для взаимодействия с данными.
* Безопасность: все данные передаются через защищенное соединение, а доступ к определенным функциям контролируется системой аутентификации.
* Гибкость: API позволяет сторонним разработчикам создавать свои собственные приложения и сервисы на основе данных Yatube.

#### Используемый стек технологий 

- [Python 3.9.10 https://docs.python.org/3.9/]
- [Django 3.2.16 https://docs.djangoproject.com/en/3.2/]
- [DRF 3.12.4 https://www.django-rest-framework.org/]
- [Simple JWT 4.7.2 https://django-rest-framework-simplejwt.readthedocs.io/en/latest/]

## Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/lordrie/api_final_yatube
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python -m venv env
```

```
source venv/Scripts/activate
```

Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```

## Примеры запросов к API

1. **Получение списка всех публикаций**
    ```
    GET /api/v1/posts/
    ```
    Пример ответа:
    ```
    {
        "count": 123,
        "next": "http://api.example.org/accounts/?offset=400&limit=100",
        "previous": "http://api.example.org/accounts/?offset=200&limit=100",
        "results": [
        {}
        ]
    }
    ```
    
2. **Добавление нового поста**
    ```
    POST .../api/v1/posts/

    {
        "text": "string",
        "image": "string",
        "group": 0
    }
    ```
    Пример ответа:
    ```
    {
        "id": 0,
        "author": "string",
        "text": "string",
        "pub_date": "2019-08-24T14:15:22Z",
        "image": "string",
        "group": 0
    }
    ```
3. **Удаление публикации**
    ```
    DELETE /api/v1/posts/{post_id}/
    ```

## Более подробное описание API можно получить по адресу:
```
http://localhost:8000/redoc/
```

#### Автор

 - [https://github.com/lordrie]