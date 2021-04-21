from uuid import uuid4
from ...db.models import user

class Get(user):
    id: str
    name: str
    surname: str

    __init__(user)
        self.id = str(user.id)
        self.name = user.first_name
        self.surname = user.last_name
