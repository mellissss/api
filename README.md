# Library API

## Описание

Library API – это RESTful API для управления книгами, авторами и жанрами.

Проект разработан на FastAPI с использованием Clean Architecture и паттерна Repository.

## Требования

Для запуска проекта необходимо:

* Python 3.10+

## Установка

1. Создайте виртуальное окружение и активируйте его

```
python -m venv venv
source venv/bin/activate    # Для Linux/Mac
venv\Scripts\activate       # Для Windows
```

2. Установите зависимости

```
pip install -r requirements.txt
```

## База данных

База данных SQLite создаётся автоматически при первом запуске.

Файл БД: `library.db` в корневой папке проекта.

## Запуск

Для запуска ввести:
```
uvicorn main:app --reload
```

Для запуска в докер:

```
docker build -t library-api .

docker run -p 8000:8000 library-api
```

Описание API будет доступно по эндпоинтам:

1. Swagger UI: http://127.0.0.1:8000/docs
2. ReDoc: http://127.0.0.1:8000/redoc

## Структура проекта

```
│
├── main.py                # Точка входа в приложение
├── database.py            # Настройка базы данных
│
├── core/                  # Бизнес-логика
│   ├── entities/          # Сущности (модели домена)
│   │   ├── author.py
│   │   ├── genre.py
│   │   └── book.py
│   │
│   ├── repositories/      # Паттерн Repository
│   │   ├── author_repo.py
│   │   ├── genre_repo.py
│   │   └── book_repo.py
│   │
│   └── services/          # Бизнес-сервисы
│       ├── author_service.py
│       ├── genre_service.py
│       └── book_service.py
│
├── api/                   # Контроллеры API
│   ├── author_api.py
│   ├── genre_api.py
│   └── book_api.py
│
└── schemas/               # Схемы для сериализации/десериализации
    ├── author_schema.py
    ├── genre_schema.py
    └── book_schema.py
```

## Тестирование

Для запуска тестов используйте команду `pytest`