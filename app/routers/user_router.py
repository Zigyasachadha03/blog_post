from fastapi import APIRouter, status, Depends
from app.database import get_db
import app.schemas.user_schema as schema
from app.services import UserService
from sqlalchemy.orm import Session
from typing import List


user_api_router = APIRouter(
    prefix='/users',
    tags= ['Users']
)

@user_api_router.get('/', response_model=List[schema.UserOut])
def get_all_users(db: Session = Depends(get_db)):
    service = UserService(db)
    return service.get_all()

@user_api_router.get('/{id}', response_model=schema.UserOut)
def get_user_by_id(id:int, db: Session = Depends(get_db)):
    service = UserService(db)
    return service.get_user_by_id(id)

@user_api_router.post('/', status_code= status.HTTP_201_CREATED, response_model=schema.UserOut)
def create_new_user(user: schema.UserCreate, db: Session = Depends(get_db)):
    service = UserService(db)
    return service.create_user(user)

@user_api_router.delete('/{id}', status_code= status.HTTP_204_NO_CONTENT)
def delete_user_by_id(id:int, db: Session = Depends(get_db)):
    service = UserService(db)
    return service.delete_user(id)

@user_api_router.put('/{id}', status_code= status.HTTP_201_CREATED, response_model=schema.UserOut)
def update_user_by_id(id:int, upd_user: schema.UserCreate ,db: Session = Depends(get_db)):
    service = UserService(db)
    return service.update_user(id, upd_user)