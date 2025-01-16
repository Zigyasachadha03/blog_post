from fastapi import APIRouter, status, Depends
from app.database import get_db
import app.schemas.user_schema as schema
from sqlalchemy.orm import Session


user_router = APIRouter(
    prefix='/users',
    tags= ['Users']
)


@user_router.post('/', status_code= status.HTTP_201_CREATED)
def create_new_user(user: schema.UserCreate, db: Session = Depends(get_db)):
    pass