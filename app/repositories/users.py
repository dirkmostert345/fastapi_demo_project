from sqlalchemy.orm import Session
from typing import List

from . import base
from ..db.models import user
from ..dtos.requests import users


class UserActions(base.BaseActions[user, users.Create, users.Update]):

    def __init__(self, model: Type[ModelType]):
        self.model = model

    def get_by_first_name(self, db: Session, *, first_name) -> List[user]:
        return db.query(self.model).filter(self.model.first_name == first_name).all()

    pass
