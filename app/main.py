# Filename: app/main.py

from fastapi import FastAPI
from app.api.v1.endpoints import auth

app = FastAPI(
    title="AI Resume Builder API",
    description="API for generating AI-powered resumes, cover letters, and more.",
    version="0.1.0",
)

# This line includes the router from auth.py
# Now that the __init__.py files exist, the import will succeed
app.include_router(auth.router, prefix="/api/v1/auth", tags=["Auth"])


@app.get("/")
async def read_root():
    """
    Root endpoint that returns a welcome message.
    """
    return {"message": "Welcome to the AI Resume Builder API!"}