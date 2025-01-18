from fastapi import APIRouter, status, Depends
from app.database import get_db
import app.schemas.user_schema as schema
from app.services import UserService
from sqlalchemy.orm import Session
from typing import List
from app.oauth2 import get_current_user


user_api_router = APIRouter(
    prefix='/users',
    tags= ['Users']
)

# @user_api_router.get('/', response_model=List[schema.UserOut])
# def get_all_users(db: Session = Depends(get_db)):
#     service = UserService(db)
#     return service.get_all()

@user_api_router.get('/', response_model=schema.UserOut)
def get_user(db: Session = Depends(get_db), current_user: schema.UserOut = Depends(get_current_user)):
    service = UserService(db)
    return service.get_user(current_user.id)

@user_api_router.post('/', status_code= status.HTTP_201_CREATED, response_model=schema.UserOut)
def create_new_user(user: schema.UserCreate, db: Session = Depends(get_db)):
    service = UserService(db)
    return service.create_user(user)

@user_api_router.delete('/', status_code= status.HTTP_204_NO_CONTENT)
def delete_user(db: Session = Depends(get_db), current_user: schema.UserOut = Depends(get_current_user)):
    service = UserService(db)
    return service.delete_user(current_user.id)

@user_api_router.put('/', status_code= status.HTTP_201_CREATED, response_model=schema.UserOut)
def update_user(upd_user: schema.UserCreate ,db: Session = Depends(get_db), current_user: schema.UserOut = Depends(get_current_user)):
    service = UserService(db)
    return service.update_user(current_user.id, upd_user)