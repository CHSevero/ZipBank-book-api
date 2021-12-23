from app.models.user import User
from app.schemas.user import User as SchemaUser
from fastapi_sqlalchemy import db
from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get(username: str):
    user = db.session.query(User).filter(User.username == username).first()
    return user


def add_user(user: SchemaUser):
    user_model = User(username=user.username, hashed_password=pwd_context.hash(user.password))
    db.session.add(user_model)
    db.session.commit()
    return user_model
