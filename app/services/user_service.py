from ..repositories.user_repository import user_repository
from typing import TypeVar, Generator
from pydantic import BaseModel, UUID4
from ..db.session import SessionLocal

from fastapi import Depends
from sqlalchemy.orm import Session


ModelType = TypeVar("ModelType", bound=BaseModel)

def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

class user_service:
    def __init__(self):
        self = self

    def get_user_by_id(id: UUID4, db: Session = Depends(get_db)):
        repo = user_repository(db=db)
        user = repo.get(db=db, id=id)
        return user