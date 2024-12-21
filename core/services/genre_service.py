from core.repositories.genre_repo import GenreRepository


class GenreService:
    def __init__(self, repository: GenreRepository):
        self.repository = repository

    def get_all_genres(self):
        """Получить все жанры"""
        return self.repository.get_all()

    def get_genre_by_id(self, genre_id: int):
        """Получить жанр по ID"""
        return self.repository.get_by_id(genre_id=genre_id)

    def create_genre(self, name: str):
        """Создать новый жанр"""
        return self.repository.create(name=name)

    def delete_genre(self, genre_id: int):
        """Удалить жанр по ID"""
        return self.repository.delete(genre_id=genre_id)
