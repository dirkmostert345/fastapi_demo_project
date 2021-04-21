from typing import Optiona
from pydantic import BaseModel, UUID4

class Create(BaseModel):
    first_name: str
    last_name: str

class Update(BaseModel):
    first_name: str
    last_name: str