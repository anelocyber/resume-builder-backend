# Filename: app/crud/user_crud.py

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

# Import your password hashing utility
from app.core.security import hash_password
# Import the SQLAlchemy model and the Pydantic schema
from app.models import user_model
from app.schemas import user_schema


async def get_user_by_email(db: AsyncSession, email: str) -> user_model.User | None:
    """
    Retrieves a user from the database by their email.
    """
    result = await db.execute(select(user_model.User).filter(user_model.User.email == email))
    return result.scalars().first()


async def create_user(db: AsyncSession, user: user_schema.UserCreate) -> user_model.User:
    """
    Creates a new user in the database.
    """
    # Securely hash the provided password
    hashed_pass = hash_password(user.password)

    # Create an instance of the SQLAlchemy User model
    db_user = user_model.User(
        email=user.email,
        name=user.name,
        hashed_password=hashed_pass
    )

    # Add the new user object to the database session
    db.add(db_user)
    # Commit the changes to the database
    await db.commit()
    # Refresh the object to get database-generated values like the UUID
    await db.refresh(db_user)
    
    return db_user