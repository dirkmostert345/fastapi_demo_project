from ..repositories.users import UserActions as userRespository
from typing import Type, TypeVar
from pydantic import BaseModel
from ..db.models import user

ModelType = TypeVar("ModelType", bound=BaseModel)

class user_service:
    def __init__(self):
        self = self

    def get_user_by_id(id):
        user = userRespository.get(id)
    