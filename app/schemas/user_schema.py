# Filename: app/schemas/user_schema.py

import uuid
from pydantic import BaseModel, EmailStr, ConfigDict

class UserBase(BaseModel):
    email: EmailStr
    name: str | None = None

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: uuid.UUID
    is_premium: bool

    # This is the modern way for Pydantic v2, which fixes the warning
    model_config = ConfigDict(from_attributes=True)