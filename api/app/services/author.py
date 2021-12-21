from app.models.author import Author as ModelAuthor
from app.schemas.author import Author as SchemaAuthor
from fastapi_sqlalchemy import db
from fastapi.encoders import jsonable_encoder
from xml.dom.minidom import parseString
from dicttoxml import dicttoxml


def add_author(author: SchemaAuthor):
    db_author = ModelAuthor(name=author.name)
    db.session.add(db_author)
    db.session.commit()
    return db_author


def authors(format):
    authors = db.session.query(ModelAuthor).all()
    if format == "xml":
        authors_json = jsonable_encoder(authors)
        authors_xml = dicttoxml(authors_json)
        return authors_xml
    return authors
