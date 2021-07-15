from fastapi import APIRouter, responses
from ...services.user_service import user_service
from ...dtos.responses import users
from pydantic import UUID4, BaseModel

router = APIRouter()

# @router.get("/{first_name}")
# async def get_user_by_firstname(first_name: str):
#     testy_westy = user_service.getUserByName(first_name)
#     return {"username:": "meh"}

@router.get(
    "/{id}",
    response_model=users.User
    )
async def get_user_by_id(id: UUID4):
    user = user_service.get_user_by_id(id)
    return user