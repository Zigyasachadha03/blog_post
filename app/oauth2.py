# from jose import JWTError
import jwt
from .config import settings
import app.schemas.login_schema as schema
from app.exception import Exceptions
from fastapi import HTTPException, status, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.services.user_service import UserService
from fastapi.security import OAuth2PasswordBearer
from datetime import datetime, timedelta
from app.models import UserModel


SECRET_KEY = settings.secret_key
ALGORITHM = settings.algorithm
ACCESS_EXPIRES_IN_MINUTES = settings.access_expires_in_minutes

def create_token(data: dict):
    to_encode = data.copy()
    expires = datetime.utcnow() + timedelta(minutes=ACCESS_EXPIRES_IN_MINUTES)
    to_encode.update({'exp': expires})
    token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return token

def verify_user(token, credentials_exception):
    try:
        payload= jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: int = payload['user_id']
        username: str = payload['username']
        if not user_id and not username:
            raise credentials_exception
        token_data = schema.TokenData(user_id=user_id,username=username)
    except jwt.PyJWTError as e:  
        print(f"Error decoding JWT token: {e}")
        raise credentials_exception
    
    return token_data


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    token_data = verify_user(token, credentials_exception)
    user = db.query(UserModel).filter(UserModel.id == token_data.user_id).first()
    if not user:
        raise credentials_exception
    return user

    
    

