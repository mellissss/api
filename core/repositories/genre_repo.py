from sqlalchemy.orm import Session
from core.entities.genre import Genre


class GenreRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(Genre).all()

    def get_by_id(self, genre_id: int):
        return self.db.query(Genre).filter(Genre.id == genre_id).first()

    def create(self, name: str):
        new_genre = Genre(name=name)
        self.db.add(new_genre)
        self.db.commit()
        self.db.refresh(new_genre)
        return new_genre

    def delete(self, genre_id: int):
        genre = self.get_by_id(genre_id)
        if genre:
            self.db.delete(genre)
            self.db.commit()
            return True
        return False
