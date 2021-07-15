from .base_repository import BaseRepository
from ..db.models import contact_detail
from ..dtos.requests import contact_details

class ContactDetailsRespository(BaseRepository[contact_detail, contact_details.Create, contact_details.Update]):
    pass

contact_details_repository = ContactDetailsRespository(contact_detail)