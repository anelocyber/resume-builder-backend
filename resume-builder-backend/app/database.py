# Filename: app/database.py

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base

from app.core.config import settings

# --- DEBUGGING LOGIC ---
# This will print the exact database URL that your application is trying to use.
# Look for this line in your terminal when the server starts.
print("--- Attempting to connect with DATABASE_URL from settings ---")
print(f"URL: '{settings.DATABASE_URL}'")
print("-------------------------------------------------------------")
# app/database.py (temporary)
print("DATABASE_URL (repr):", repr(settings.DATABASE_URL))


# Create an asynchronous engine to connect to the database.
engine = create_async_engine(
    settings.DATABASE_URL,
    echo=True,
)

# ... (the rest of the file is the same)
AsyncSessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)

Base = declarative_base()

async def get_db() -> AsyncSession:
    async with AsyncSessionLocal() as session:
        yield session