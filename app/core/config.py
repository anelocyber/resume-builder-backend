import os
from pydantic_settings import BaseSettings

# This line is for local development if you haven't set up a full .env structure yet
# from dotenv import load_dotenv
# load_dotenv()

class Settings(BaseSettings):
    # Supabase Database URL
    # The variable name MUST match the one in your .env file (case-sensitive)
    DATABASE_URL: str

    # JWT Settings
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    # Add other settings from your .env file as needed
    # SENDGRID_API_KEY: str
    # OPENAI_API_KEY: str

    class Config:
        # This tells pydantic-settings to load variables from a .env file
        env_file = ".env"

# Create a single, importable instance of the settings
settings = Settings()