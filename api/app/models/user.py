from sqlalchemy import Boolean, Column, DateTime, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    email = Column(String, nullable=True)
    full_name = Column(String, nullable=True)
    disabled = Column(Boolean, default=False)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())
