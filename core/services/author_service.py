from core.repositories.author_repo import AuthorRepository


class AuthorService:
    def __init__(self, repository: AuthorRepository):
        self.repository = repository

    def get_all_authors(self):
        """Получить всех авторов"""
        return self.repository.get_all()

    def get_author_by_id(self, author_id: int):
        """Получить автора по ID"""
        return self.repository.get_by_id(author_id=author_id)

    def create_author(self, name: str, birth_year: int):
        """Создать нового автора"""
        return self.repository.create(name=name, birth_year=birth_year)

    def delete_author(self, author_id: int):
        """Удалить автора по ID"""
        return self.repository.delete(author_id=author_id)
