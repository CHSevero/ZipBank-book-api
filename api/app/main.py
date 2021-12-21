import os

from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware
from .routers.author import router as author_router

app = FastAPI()

app.add_middleware(DBSessionMiddleware, db_url=os.environ["DATABASE_URL"])
app.include_router(author_router)


@app.get("/", tags=["Book-API"])
def root():
    return {"message": "Book-API alive!"}