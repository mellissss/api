from fastapi import APIRouter, Depends
from core.services.author_service import AuthorService
from core.repositories.author_repo import AuthorRepository
from database import SessionLocal

router = APIRouter()


def get_service():
    db = SessionLocal()
    return AuthorService(AuthorRepository(db))


@router.get(
    "/", summary="Get all authors", description="Retrieve a list of all authors."
)
def get_authors(service: AuthorService = Depends(get_service)):
    return service.get_all_authors()


@router.get(
    "/{author_id}",
    summary="Get an author by ID",
    description="Retrieve a single author by its ID.",
)
def get_author(author_id: int, service: AuthorService = Depends(get_service)):
    return service.get_author_by_id(author_id)


@router.post(
    "/", summary="Create a new author", description="Add a new author to the database."
)
def create_author(
    name: str, birth_year: int, service: AuthorService = Depends(get_service)
):
    return service.create_author(name, birth_year)


@router.delete(
    "/{author_id}",
    summary="Delete an author",
    description="Remove an author by its ID.",
)
def delete_author(author_id: int, service: AuthorService = Depends(get_service)):
    return service.delete_author(author_id)
