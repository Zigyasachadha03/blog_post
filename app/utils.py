from passlib.context import CryptContext
import argon2

pwd_context = CryptContext(schemes=['argon2'])

def hash_password(password: str):
    return pwd_context.hash(password)
