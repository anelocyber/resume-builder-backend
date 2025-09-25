# Filename: app/models/user_model.py

from sqlalchemy import Column, String, Boolean, text
from sqlalchemy.dialects.postgresql import UUID

# Import the Base class from your database setup file
from app.database import Base

class User(Base):
    # This name must match your actual table name in Supabase/PostgreSQL
    __tablename__ = "users"

    # Define the columns for the 'users' table
    id = Column(UUID(as_uuid=True), primary_key=True, server_default=text("gen_random_uuid()"))
    email = Column(String, nullable=False, unique=True, index=True)
    hashed_password = Column(String, nullable=False)
    name = Column(String, nullable=True)
    is_premium = Column(Boolean, server_default="false", nullable=False)