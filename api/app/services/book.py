from app.models.book import Book
from app.schemas.book import Book as SchemaBook
from fastapi_sqlalchemy import db


def add_book(book: SchemaBook):
    model_book = Book(title=book.title,
                      description=book.description,
                      author_id=book.author_id
                      )
    db.session.add(model_book)
    db.session.commit()
    return model_book

