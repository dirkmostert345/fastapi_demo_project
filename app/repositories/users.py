from sqlalchemy.orm import Session
from typing import List, Type, TypeVar
from pydantic import BaseModel
from fastapi import Depends

from . import base
from ..db.models import user
from ..dtos.requests import users

ModelType = TypeVar("ModelType", bound=BaseModel)

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

class UserActions(base.BaseActions[user, users.Create, users.Update]):

    def __init__(self, model: Type[ModelType]):
        self.model = model

    def get_by_first_name(self, first_name) -> List[user]:
        print(first_name)
        return Depends(get_db).query(self.model).filter(self.model.first_name == first_name).all()

    pass
