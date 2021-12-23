from fastapi import APIRouter
from app.schemas.user import User as SchemaUser
from app.services import user as service_user
router = APIRouter()


@router.post("/add-user/", tags=["User"])
async def add_user(user: SchemaUser):
    return service_user.add_user(user)
