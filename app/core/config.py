# Filename: app/core/config.py

from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # This tells Pydantic to expect these variables from the environment (.env file)
    DATABASE_URL: str
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    class Config:
        # This single line tells pydantic-settings to load from a .env file.
        # It automatically finds it in your project's root directory.
        env_file = ".env"

# Create one instance of the settings that the rest of your app can import and use
settings = Settings()