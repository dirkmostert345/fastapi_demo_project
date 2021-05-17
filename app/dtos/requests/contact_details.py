from pydantic import BaseModel, UUID4

class ContactDetailBase(BaseModel):
    id: UUID4
    user_id : UUID4
    phone_number: str
    email_address: str

class Create(ContactDetailBase):
    pass

class Update(ContactDetailBase):
    pass

class ContactDetails(ContactDetailBase):
    pass

    class Config:
        orm_mode = True