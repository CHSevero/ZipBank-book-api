from fastapi import APIRouter
from app.schemas.author import Author as SchemaAuthor
from app.services import author as author_service

router = APIRouter()


@router.post("/add-author/", tags=["Author"], response_model=SchemaAuthor)
def add_author(author: SchemaAuthor):
    return author_service.add_author(author)
