import pytest
from unittest.mock import Mock
from core.services.author_service import AuthorService
from core.repositories.author_repo import AuthorRepository


@pytest.fixture
def mock_repo():
    return Mock(spec=AuthorRepository)


@pytest.fixture
def service(mock_repo):
    return AuthorService(mock_repo)


def test_get_all_authors(service, mock_repo):
    mock_repo.get_all.return_value = [{"id": 1, "name": "John", "birth_year": 1980}]
    authors = service.get_all_authors()
    assert len(authors) == 1
    assert authors[0]["name"] == "John"
    mock_repo.get_all.assert_called_once()


def test_get_author_by_id(service, mock_repo):
    mock_repo.get_by_id.return_value = {"id": 1, "name": "John", "birth_year": 1980}
    author = service.get_author_by_id(author_id=1)
    assert author["id"] == 1
    mock_repo.get_by_id.assert_called_once_with(author_id=1)


def test_get_author_by_id_not_found(service, mock_repo):
    mock_repo.get_by_id.return_value = None
    author = service.get_author_by_id(author_id=999)
    assert author is None
    mock_repo.get_by_id.assert_called_once_with(author_id=999)


def test_create_author(service, mock_repo):
    mock_repo.create.return_value = {"id": 1, "name": "John", "birth_year": 1980}
    author = service.create_author(name="John", birth_year=1980)
    assert author["name"] == "John"
    mock_repo.create.assert_called_once_with(name="John", birth_year=1980)


def test_delete_author(service, mock_repo):
    mock_repo.delete.return_value = True
    result = service.delete_author(author_id=1)
    assert result is True
    mock_repo.delete.assert_called_once_with(author_id=1)


def test_delete_author_not_found(service, mock_repo):
    mock_repo.delete.return_value = False
    result = service.delete_author(author_id=999)
    assert result is False
    mock_repo.delete.assert_called_once_with(author_id=999)
