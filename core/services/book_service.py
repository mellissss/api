from core.repositories.book_repo import BookRepository


class BookService:
    def __init__(self, repository: BookRepository):
        self.repository = repository

    def get_all_books(self):
        """Получить все книги"""
        return self.repository.get_all()

    def get_book_by_id(self, book_id: int):
        """Получить книгу по ID"""
        return self.repository.get_by_id(book_id=book_id)

    def create_book(self, title: str, author_id: int, genre_id: int):
        """Создать новую книгу"""
        return self.repository.create(title=title, author_id=author_id, genre_id=genre_id)

    def delete_book(self, book_id: int):
        """Удалить книгу по ID"""
        return self.repository.delete(book_id=book_id)
