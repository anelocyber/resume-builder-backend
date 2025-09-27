📄 README: Resume Builder Backend with Supabase Auth
This is a FastAPI backend for a resume builder application. It uses Supabase for authentication and user metadata storage. This guide walks you through setting up the project, connecting to Supabase, and registering your first user.

🚀 Features
Supabase Auth integration for secure user registration and login

FastAPI endpoints for /register and /login

Password hashing using Passlib

Metadata storage in Supabase users table

🧰 Prerequisites
Python 3.11+

Supabase account: https://supabase.com

Git & GitHub (optional)

VS Code or any IDE

🛠️ Setup Instructions
1. Clone the repository
bash
git clone https://github.com/your-username/resume-builder-backend.git
cd resume-builder-backend
2. Create and activate a virtual environment
bash
python -m venv .venv
.\.venv\Scripts\activate  # On Windows
3. Install dependencies
bash
pip install -r requirements.txt
🔐 Supabase Setup
1. Create a Supabase project
Go to https://app.supabase.com

Click New Project

Choose a name, password, and region

Wait for the project to initialize

2. Get your Supabase credentials
Go to Project Settings → API

Copy:

Project URL

Service Role Key

3. Create a users table
In Supabase SQL Editor, run:

sql
create table users (
  id uuid default gen_random_uuid() primary key,
  email text unique not null,
  hashed_password text not null,
  name text,
  created_at timestamp default now()
);
📦 Environment Configuration
Create a .env file in the root directory:

env
DATABASE_URL="postgresql+asyncpg://postgres:your-db-password@db.your-project.supabase.co:5432/postgres"

SECRET_KEY="your-secret-key"
ALGORITHM="HS256"
ACCESS_TOKEN_EXPIRE_MINUTES=30

SUPABASE_URL="https://your-project.supabase.co"
SUPABASE_KEY="your-service-role-key"
Replace all placeholder values with your actual Supabase credentials.

🧪 Run the Server
bash
uvicorn app.main:app --reload
Visit http://localhost:8000/docs to access Swagger UI.

🧍 Register Your First User
In Swagger UI:

Go to POST /api/v1/auth/register

Click "Try it out"

Enter:

json
{
  "email": "your-email@example.com",
  "password": "StrongPassword123!",
  "name": "Emma"
}
Click "Execute"

You should see a successful response and the user will be added to both Supabase Auth and the users table.

🔑 Login
Use POST /api/v1/auth/login with your email and password to receive a JWT access token.

🧼 Optional Enhancements
Add /me endpoint to fetch user profile

Connect to a frontend (React, Next.js, etc.)

Deploy to Render, Railway, or Vercel