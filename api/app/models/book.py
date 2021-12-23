from sqlalchemy import Column, DateTime, ForeignKey, Integer,String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from .author import Author
Base = declarative_base()


class Book(Base):
    __tablename__ = "book"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())
    author_id = Column(Integer, ForeignKey(Author.id))
    author = relationship(Author)
