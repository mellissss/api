from fastapi import APIRouter, Depends
from core.services.genre_service import GenreService
from core.repositories.genre_repo import GenreRepository
from database import SessionLocal

router = APIRouter()


def get_service():
    db = SessionLocal()
    return GenreService(GenreRepository(db))


@router.get("/", summary="Get all genres", description="Retrieve a list of all genres.")
def get_genres(service: GenreService = Depends(get_service)):
    return service.get_all_genres()


@router.get(
    "/{genre_id}",
    summary="Get a genre by ID",
    description="Retrieve a single genre by its ID.",
)
def get_genre(genre_id: int, service: GenreService = Depends(get_service)):
    return service.get_genre_by_id(genre_id)


@router.post(
    "/", summary="Create a new genre", description="Add a new genre to the database."
)
def create_genre(name: str, service: GenreService = Depends(get_service)):
    return service.create_genre(name)


@router.delete(
    "/{genre_id}", summary="Delete a genre", description="Remove a genre by its ID."
)
def delete_genre(genre_id: int, service: GenreService = Depends(get_service)):
    return service.delete_genre(genre_id)
