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


def get_book(book_id: int):
    book = db.session.get(Book, {"id": book_id})
    return book


def update_book(book_id: int, book: SchemaBook):
    book_db = db.session.get(Book, {"id": book_id})
    if book_db:
        book_db.title = book.title
        book_db.description = book.description
        book_db.author_id = book.author_id
    return book_db


def delete_book(book_id: int):
    book_db = db.session.get(Book, {"id": book_id})
    if book_db:
        db.session.delete(book_db)
        db.session.commit()
    return book_db
