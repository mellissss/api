import pytest
from unittest.mock import Mock
from core.services.book_service import BookService
from core.repositories.book_repo import BookRepository


@pytest.fixture
def mock_repo():
    return Mock(spec=BookRepository)


@pytest.fixture
def service(mock_repo):
    return BookService(mock_repo)


def test_get_all_books(service, mock_repo):
    mock_repo.get_all.return_value = [
        {"id": 1, "title": "1984", "author_id": 1, "genre_id": 1}
    ]
    books = service.get_all_books()
    assert len(books) == 1
    assert books[0]["title"] == "1984"
    mock_repo.get_all.assert_called_once()


def test_get_book_by_id(service, mock_repo):
    mock_repo.get_by_id.return_value = {"id": 1, "title": "1984", "author_id": 1, "genre_id": 1}
    book = service.get_book_by_id(book_id=1)
    assert book["title"] == "1984"
    mock_repo.get_by_id.assert_called_once_with(book_id=1)


def test_get_book_by_id_not_found(service, mock_repo):
    mock_repo.get_by_id.return_value = None
    book = service.get_book_by_id(book_id=999)
    assert book is None
    mock_repo.get_by_id.assert_called_once_with(book_id=999)


def test_create_book(service, mock_repo):
    mock_repo.create.return_value = {"id": 1, "title": "1984", "author_id": 1, "genre_id": 1}
    book = service.create_book(title="1984", author_id=1, genre_id=1)
    assert book["title"] == "1984"
    mock_repo.create.assert_called_once_with(title="1984", author_id=1, genre_id=1)


def test_delete_book(service, mock_repo):
    mock_repo.delete.return_value = True
    result = service.delete_book(book_id=1)
    assert result is True
    mock_repo.delete.assert_called_once_with(book_id=1)


def test_delete_book_not_found(service, mock_repo):
    mock_repo.delete.return_value = False
    result = service.delete_book(book_id=999)
    assert result is False
    mock_repo.delete.assert_called_once_with(book_id=999)
