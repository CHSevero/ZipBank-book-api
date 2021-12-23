from fastapi import APIRouter, Depends
from app.schemas.book import Book as SchemaBook
from app.services.auth import get_current_active_user
from app.services import book as service_book

router = APIRouter()


@router.post("/add-book/", tags=["Book"], response_model=SchemaBook)
def add_book(book: SchemaBook,
             token: str = Depends(get_current_active_user)
             ):
    return service_book.add_book(book)
