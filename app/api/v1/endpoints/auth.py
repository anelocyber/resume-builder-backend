# Filename: app/api/v1/endpoints/auth.py

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud import user_crud
from app.schemas import user_schema
from app.database import get_db

router = APIRouter()

# THE TYPO IS FIXED HERE: HTTP_2_CREATED -> HTTP_201_CREATED
@router.post("/register", response_model=user_schema.User, status_code=status.HTTP_201_CREATED)
async def register_user(
    user_in: user_schema.UserCreate,
    db: AsyncSession = Depends(get_db)
):
    """
    Register a new user.
    """
    db_user = await user_crud.get_user_by_email(db, email=user_in.email)
    if db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="An account with this email already exists.",
        )
        
    new_user = await user_crud.create_user(db=db, user=user_in)
    return new_user