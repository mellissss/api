import pytest
from unittest.mock import Mock
from core.services.genre_service import GenreService
from core.repositories.genre_repo import GenreRepository


@pytest.fixture
def mock_repo():
    return Mock(spec=GenreRepository)


@pytest.fixture
def service(mock_repo):
    return GenreService(mock_repo)


def test_get_all_genres(service, mock_repo):
    mock_repo.get_all.return_value = [{"id": 1, "name": "Fiction"}]
    genres = service.get_all_genres()
    assert len(genres) == 1
    assert genres[0]["name"] == "Fiction"
    mock_repo.get_all.assert_called_once()


def test_get_genre_by_id(service, mock_repo):
    mock_repo.get_by_id.return_value = {"id": 1, "name": "Fiction"}
    genre = service.get_genre_by_id(genre_id=1)
    assert genre["name"] == "Fiction"
    mock_repo.get_by_id.assert_called_once_with(genre_id=1)


def test_get_genre_by_id_not_found(service, mock_repo):
    mock_repo.get_by_id.return_value = None
    genre = service.get_genre_by_id(genre_id=999)
    assert genre is None
    mock_repo.get_by_id.assert_called_once_with(genre_id=999)


def test_create_genre(service, mock_repo):
    mock_repo.create.return_value = {"id": 1, "name": "Fiction"}
    genre = service.create_genre(name="Fiction")
    assert genre["name"] == "Fiction"
    mock_repo.create.assert_called_once_with(name="Fiction")


def test_delete_genre(service, mock_repo):
    mock_repo.delete.return_value = True
    result = service.delete_genre(genre_id=1)
    assert result is True
    mock_repo.delete.assert_called_once_with(genre_id=1)


def test_delete_genre_not_found(service, mock_repo):
    mock_repo.delete.return_value = False
    result = service.delete_genre(genre_id=999)
    assert result is False
    mock_repo.delete.assert_called_once_with(genre_id=999)
