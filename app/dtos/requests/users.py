from pydantic import BaseModel, UUID4

class UserBase(BaseModel):
    id: UUID4
    first_name: str
    last_name: str

class Create(UserBase):
    pass

class Update(UserBase):
    pass

class User(UserBase):
    pass

    class Config:
        orm_mode = True