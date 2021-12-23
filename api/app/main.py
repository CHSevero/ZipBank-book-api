import os

from fastapi import Depends, FastAPI
from .services.auth import get_current_active_user
from fastapi_sqlalchemy import DBSessionMiddleware
from .routers.author import router as author_router
from .routers.auth import router as auth_router
from .routers.user import router as user_router

app = FastAPI()


app.add_middleware(DBSessionMiddleware, db_url=os.environ["DATABASE_URL"])
app.include_router(auth_router)
app.include_router(author_router)
app.include_router(user_router)


@app.get("/", tags=["Book-API"])
def root(token: str = Depends(get_current_active_user)):
    return {"message": "Book-API alive!"}
