from passlib.context import CryptContext

# Create a CryptContext instance, specifying the hashing algorithm
# "bcrypt" is a strong, widely-used hashing algorithm.
# The "auto" scheme will automatically use the default scheme (bcrypt).
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verifies a plain-text password against a hashed password."""
    return pwd_context.verify(plain_password, hashed_password)

def hash_password(password: str) -> str:
    """Hashes a plain-text password."""
    return pwd_context.hash(password)