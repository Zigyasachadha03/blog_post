from passlib.context import CryptContext
import argon2

pwd_context = CryptContext(schemes=['argon2'], deprecated="auto")

def hash_password(password: str):
    return pwd_context.hash(password)

def verify_password(password: str, hashed_password: str):
    return pwd_context.verify(password, hashed_password)
