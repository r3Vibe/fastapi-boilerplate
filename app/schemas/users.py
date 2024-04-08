from pydantic import BaseModel, Field, EmailStr


class UserRegistration(BaseModel):
    name: str = Field(title="Name")
    email: EmailStr = Field(title="Email")
