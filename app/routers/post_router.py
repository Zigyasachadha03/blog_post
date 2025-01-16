from fastapi import APIRouter, Depends, status
import app.schemas.post_schema as schema
from app.services import PostService
from app.database import get_db
from sqlalchemy.orm import Session
from typing import List


post_router = APIRouter(
    prefix='/posts',
    tags= ['Posts']
)



@post_router.get('/{id}', response_model = schema.PostOut)
def get_post_by_id(id: int, db:Session = Depends(get_db)):
    post_service = PostService(db)
    post = post_service.get_post_by_id(id)
    return post

@post_router.get('/', response_model = List[schema.PostOut])
def get_all_posts(db:Session = Depends(get_db)):
    post_service = PostService(db)
    return post_service.get_all()

@post_router.post('/', response_model = schema.PostOut, status_code= status.HTTP_201_CREATED)
def create_new_post(new_post: schema.PostCreate, db:Session = Depends(get_db)):
    post_service = PostService(db)
    return post_service.create_post(new_post)


@post_router.delete('/{id}', status_code= status.HTTP_204_NO_CONTENT)
def delete_post_by_id(id: int, db:Session = Depends(get_db)):
    post_service = PostService(db)
    return post_service.delete_post(id)


@post_router.put('/{id}', status_code= status.HTTP_202_ACCEPTED, response_model= schema.PostOut)
def update_post_by_id(id: int, upd_post: schema.PostCreate, db: Session = Depends(get_db)):
    post_service = PostService(db)
    return post_service.update_post(id, upd_post)