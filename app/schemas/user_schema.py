from pydantic import BaseModel, EmailStr

class UserCreate:
    username: str
    email: EmailStr
    password: str