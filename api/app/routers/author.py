from typing import Optional
from fastapi import APIRouter, Depends
from app.schemas.author import Author as SchemaAuthor
from app.services import author as author_service
from app.services.auth import oauth2_scheme

router = APIRouter()


@router.post("/add-author/", tags=["Author"], response_model=SchemaAuthor)
def add_author(author: SchemaAuthor):
    return author_service.add_author(author)


@router.get("/authors/", tags=["Author"])
def get_authors(format: Optional[str] = None,
                page: Optional[int] = 1,
                size: Optional[int] = 10,
                token: str = Depends(oauth2_scheme)
                ):
    return author_service.authors(format, page, size)


@router.get("/author/{id}", tags=["Author"])
def get_author_by_id(id: int, format: Optional[str] = None):
    return author_service.author(id, format)


@router.put("/author/{id}", tags=["Author"], response_model=SchemaAuthor)
def update_author(id: int, author: SchemaAuthor, format: Optional[str] = None):
    return author_service.update_author(id, author, format)


@router.delete("/author/{id}", tags=["Author"])
def delete_author(id: int):
    return author_service.delete_author(id)
