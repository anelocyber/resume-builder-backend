import uuid
from pydantic import BaseModel, EmailStr

# --- Base Schema ---
# Shared properties that are common to all user-related schemas.
class UserBase(BaseModel):
    email: EmailStr
    name: str | None = None # This means the name is an optional string

# --- Schemas for Receiving Data (from client to API) ---
# Properties to receive via API on user creation.
class UserCreate(UserBase):
    password: str

# --- Schemas for Sending Data (from API to client) ---
# Properties to return to the client.
# IMPORTANT: Never include the password here.
class User(UserBase):
    id: uuid.UUID
    is_premium: bool

    class Config:
        # This tells Pydantic to read the data even if it is not a dict,
        # but an ORM model (or any other arbitrary object with attributes).
        orm_mode = True