import os

from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer
from fastapi_sqlalchemy import DBSessionMiddleware
from .routers.author import router as author_router

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app.add_middleware(DBSessionMiddleware, db_url=os.environ["DATABASE_URL"])
app.include_router(author_router)


@app.get("/", tags=["Book-API"])
def root(token: str = Depends(oauth2_scheme)):
    return {"message": "Book-API alive!"}
