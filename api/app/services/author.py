from app.models.author import Author as ModelAuthor
from app.schemas.author import Author as SchemaAuthor
from fastapi_sqlalchemy import db


def add_author(author: SchemaAuthor):
    db_author = ModelAuthor(name=author.name)
    db.session.add(db_author)
    db.session.commit()
    return db_author