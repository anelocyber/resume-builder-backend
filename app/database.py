from sqlalchemy.ext.asyncio import create_async_engine, sessionmaker, AsyncSession
from sqlalchemy.orm import declarative_base

from app.core.config import settings

# Create an asynchronous engine to connect to the database
# The engine is the starting point for any SQLAlchemy application.
engine = create_async_engine(
    settings.DATABASE_URL,
    echo=True,  # Set to False in production
)

# Create a sessionmaker factory that will produce new AsyncSession objects
# A session is the primary interface for all database operations (queries, commits, etc.)
AsyncSessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)

# Create a Base class for our declarative models
# All of our database table models will inherit from this class.
Base = declarative_base()

# Dependency to get a DB session
# This function will be used in our API endpoints to get a database session.
async def get_db() -> AsyncSession:
    async with AsyncSessionLocal() as session:
        yield session