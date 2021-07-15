from .base_repository import BaseRepository
from ..db.models import user
from ..dtos.requests import users

class UserRepository(BaseRepository[user, users.Create, users.Update]):
    pass

user_repository = UserRepository(user)