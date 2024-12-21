from fastapi import FastAPI

from database import engine
from api.author_api import router as author_router
from api.genre_api import router as genre_router
from api.book_api import router as book_router
from core.entities.author import Author
from core.entities.genre import Genre
from core.entities.book import Book

# Создание таблиц
Author.__table__.create(engine, checkfirst=True)
Genre.__table__.create(engine, checkfirst=True)
Book.__table__.create(engine, checkfirst=True)

# Создание экземпляра приложения
app = FastAPI(
    title="Library API",
    description="API для управления книгами, авторами и жанрами",
    version="1.0.0",
)

# Подключение маршрутов API
app.include_router(author_router, prefix="/authors", tags=["Authors"])
app.include_router(genre_router, prefix="/genres", tags=["Genres"])
app.include_router(book_router, prefix="/books", tags=["Books"])


# Корневой эндпоинт
@app.get(
    "/", summary="Root endpoint", description="Возвращает приветственное сообщение"
)
def read_root():
    return {"message": "Welcome to the Library API"}


# Точка запуска приложения
if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
