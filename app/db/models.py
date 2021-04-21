from uuid import uuid4
from sqlalchemy import Column, String, Text, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from . import Base


class user(Base):
    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid4)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    contact_details = relationship("contact_detail", backref="users")

class contact_detail(Base):
    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid4)
    user_id = Column(UUID, ForeignKey('users.id'))
    user = relationship("user", backref="contact_details")
    phone_number=Column(String(20), nullable=True)
    email_address=Column(String(30), nullable=True)