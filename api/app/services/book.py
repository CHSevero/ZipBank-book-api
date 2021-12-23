from app.models.book import Book
from app.schemas.book import Book as SchemaBook
from fastapi_sqlalchemy import db
from app.utils.pagination import paginate

def add_book(book: SchemaBook):
    model_book = Book(title=book.title,
                      description=book.description,
                      author_id=book.author_id
                      )
    db.session.add(model_book)
    db.session.commit()
    return model_book


def get_books(page: int, size: int):
    books = db.session.query(Book).all()
    paginated_books = paginate(books, page, size)
    return paginated_books

