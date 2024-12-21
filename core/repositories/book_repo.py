from sqlalchemy.orm import Session
from core.entities.book import Book


class BookRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(Book).all()

    def get_by_id(self, book_id: int):
        return self.db.query(Book).filter(Book.id == book_id).first()

    def create(self, title: str, author_id: int, genre_id: int):
        new_book = Book(title=title, author_id=author_id, genre_id=genre_id)
        self.db.add(new_book)
        self.db.commit()
        self.db.refresh(new_book)
        return new_book

    def delete(self, book_id: int):
        book = self.get_by_id(book_id)
        if book:
            self.db.delete(book)
            self.db.commit()
            return True
        return False
