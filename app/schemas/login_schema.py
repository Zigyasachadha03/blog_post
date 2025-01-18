from pydantic import BaseModel
from typing import Optional

class LoginCredetials(BaseModel):
    username: str
    password: str


class TokenData(BaseModel):
    user_id: Optional[int]
    username: Optional[str]

class Token(BaseModel):
    access_token: str
    access_type: str = 'Bearer'