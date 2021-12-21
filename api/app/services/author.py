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


def author(id, format):

    author_ = db.session.get(ModelAuthor, {"id": id})
    if author_ is not None:
        if format == "xml":
            author_json = jsonable_encoder(author_)
            return dicttoxml(author_json)
        return author_

    message = {"message": f"Author with id: {id} does not exists!"}
    if format == "xml":
        message_json = jsonable_encoder(message)
        return dicttoxml(message_json)
    return message


def update_author(id, author, format):
    author_ = db.session.get(ModelAuthor, {"id": id})
    if author_ is not None:
        author_.name = author.name
        db.session.commit()
        if format == "xml":
            author_json = jsonable_encoder(author_)
            return dicttoxml(author_json)
        return author_

    message = {"message": f"Author with id: {id} does not exists!"}
    if format == "xml":
        message_json = jsonable_encoder(message)
        return dicttoxml(message_json)
    return message


def delete_author(id):
    author_ = db.session.get(ModelAuthor, {"id": id})
    if author_ is not None:
        db.session.delete(author_)
        db.session.commit()
        return author_
    return {"message": f"Author with id: {id} does not exists!"}
