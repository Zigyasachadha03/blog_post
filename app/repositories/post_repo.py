from app.repositories import BaseRepository
from app.models import PostModel
from app.schemas import PostCreate
from app import Exceptions
from sqlalchemy.orm import Session
from sqlalchemy import select

class PostRespository(BaseRepository):

    def __init__(self, db: Session):
        self.db = db

    def find_by_id(self, id: int):
        post = self.db.query(PostModel).filter(PostModel.id == id).first()
        if not post:
            raise Exceptions.exception_404()
        return post
    
    def find_all(self):
        posts = self.db.query(PostModel).all()
        return posts
    
    def save(self, new_post: PostCreate):
        post = PostModel(**dict(new_post))
        self.db.add(post)
        self.db.commit()
        self.db.refresh(post)

        return post

    def delete(self, id: int):
        post = self.db.query(PostModel).filter(PostModel.id == id)
        if not post.first():
            raise Exceptions.exception_404()
        post.delete(synchronize_session=False)
        return
    
    def update(self, id: int, upd_post: PostCreate):
        post = self.db.query(PostModel).filter(PostModel.id == id)

        if not post.first():
            raise Exceptions.exception_404()
        
        post.update(dict(upd_post))
        self.db.commit()
        return post.first()
    
    