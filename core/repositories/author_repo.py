from sqlalchemy.orm import Session
from core.entities.author import Author


class AuthorRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(Author).all()

    def get_by_id(self, author_id: int):
        return self.db.query(Author).filter(Author.id == author_id).first()

    def create(self, name: str, birth_year: int):
        new_author = Author(name=name, birth_year=birth_year)
        self.db.add(new_author)
        self.db.commit()
        self.db.refresh(new_author)
        return new_author

    def delete(self, author_id: int):
        author = self.get_by_id(author_id)
        if author:
            self.db.delete(author)
            self.db.commit()
            return True
        return False
