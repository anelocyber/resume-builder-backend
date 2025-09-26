from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordRequestForm
from app.schemas import user_schema
from app.core.config import settings
from app.core import security
from supabase import create_client, Client

router = APIRouter()

# Initialize Supabase client
supabase: Client = create_client(settings.SUPABASE_URL, settings.SUPABASE_KEY)

@router.post("/register", response_model=user_schema.User, status_code=status.HTTP_201_CREATED)
async def register_user(user_in: user_schema.UserCreate):
    """
    Register a new user using Supabase Auth and insert metadata into 'users' table.
    """
    # 1. Register user via Supabase Auth
    response = supabase.auth.sign_up({
        "email": user_in.email,
        "password": user_in.password
    })

    response_data = response.model_dump()
    if response_data.get("error"):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=response_data["error"]["message"]
        )

    # 2. Check for duplicate in metadata table
    existing_user = supabase.table("users").select("id").eq("email", user_in.email).execute()
    existing_data = existing_user.model_dump()
    if existing_data.get("data"):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User already exists in metadata table."
        )

    # 3. Hash password and insert metadata
    hashed_password = security.hash_password(user_in.password)
    insert_response = supabase.table("users").insert({
        "email": user_in.email,
        "name": user_in.name,
        "hashed_password": hashed_password
    }).execute()

    insert_data = insert_response.model_dump()
    if insert_data.get("status_code", 200) >= 400:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="User created in Auth but failed to insert into users table."
        )

    return {
        "email": user_in.email,
        "name": user_in.name
    }

@router.post("/login", response_model=user_schema.Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    """
    Authenticate user using Supabase Auth and return a JWT access token.
    """
    response = supabase.auth.sign_in_with_password({
        "email": form_data.username,
        "password": form_data.password
    })

    response_data = response.model_dump()
    if response_data.get("error"):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    session = response_data.get("session")
    if not session or not session.get("access_token"):
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Login succeeded but no access token returned"
        )

    return {
        "access_token": session["access_token"],
        "token_type": "bearer"
    }
