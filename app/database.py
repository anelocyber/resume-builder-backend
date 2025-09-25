# Filename: app/database.py

# CORRECTED IMPORTS FOR MODERN SQLAlchemy (v2.0+)
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base

# Import the settings object which contains your DATABASE_URL
from app.core.config import settings

# Create an asynchronous engine to connect to the database.
engine = create_async_engine(
    settings.DATABASE_URL,
    echo=True,  # Log SQL queries. Set to False in production.
)

# Create a configured "AsyncSession" class.
# We now import sessionmaker from sqlalchemy.orm
AsyncSessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)

# Create a Base class for our ORM models to inherit from.
Base = declarative_base()


# Dependency function to get a DB session for each API request.
async def get_db() -> AsyncSession:
    async with AsyncSessionLocal() as session:
        yield session