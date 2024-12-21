from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# URL для подключения к базе данных SQLite
DATABASE_URL = "sqlite:///library.db"

# Создание движка для БД
engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}, echo=True
)

# Базовый класс для всех моделей ORM
Base = declarative_base()

# Сессия для работы с БД
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

if __name__ == '__main__':
    from core.entities.author import Author
    from core.entities.book import Book
    from core.entities.genre import Genre

    # Создание таблиц
    Author.__table__.create(engine, checkfirst=True)
    Genre.__table__.create(engine, checkfirst=True)
    Book.__table__.create(engine, checkfirst=True)
