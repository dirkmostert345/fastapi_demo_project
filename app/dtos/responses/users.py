from uuid import uuid4
from ...db.models import user
from pydantic import BaseModel

class UserBase(BaseModel):
    name: str
    surname: str
class User(UserBase):
    id: str
    
    class Config:
        orm_mode = True

