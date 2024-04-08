from beanie import Document, Indexed
from pydantic import Field, EmailStr
from datetime import datetime
from uuid import UUID, uuid4
from typing import Annotated


class Users(Document):
    id: UUID = Field(default_factory=uuid4)
    name: str
    email: Annotated[EmailStr, Indexed(unique=True)]
    created: datetime = Field(default_factory=datetime.now)

    class Settings:
        name = "users"
