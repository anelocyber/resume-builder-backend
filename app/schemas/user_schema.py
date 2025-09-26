# Filename: app/schemas/user_schema.py

from pydantic import BaseModel, EmailStr

# --- Schemas for Receiving Data (from client to API) ---
class UserCreate(BaseModel):
    email: EmailStr
    password: str
    name: str

# --- Schemas for Sending Data (from API to client) ---
class User(BaseModel):
    email: EmailStr
    name: str

# --- Schema for JWT Token ---
class Token(BaseModel):
    access_token: str
    token_type: str