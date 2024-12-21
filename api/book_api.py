from fastapi import APIRouter, Depends
from core.services.book_service import BookService
from core.repositories.book_repo import BookRepository
from database import SessionLocal

router = APIRouter()


def get_service():
    db = SessionLocal()
    return BookService(BookRepository(db))


@router.get("/", summary="Get all books", description="Retrieve a list of all books.")
def get_books(service: BookService = Depends(get_service)):
    return service.get_all_books()


@router.get(
    "/{book_id}",
    summary="Get a book by ID",
    description="Retrieve a single book by its ID.",
)
def get_book(book_id: int, service: BookService = Depends(get_service)):
    return service.get_book_by_id(book_id)


@router.post(
    "/", summary="Create a new book", description="Add a new book to the database."
)
def create_book(
    title: str,
    author_id: int,
    genre_id: int,
    service: BookService = Depends(get_service),
):
    return service.create_book(title, author_id, genre_id)


@router.delete(
    "/{book_id}", summary="Delete a book", description="Remove a book by its ID."
)
def delete_book(book_id: int, service: BookService = Depends(get_service)):
    return service.delete_book(book_id)
