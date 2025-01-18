from app.repositories import BaseRepository
from app.models import PostModel
from app.schemas import PostCreate
from app import Exceptions
from sqlalchemy.orm import Session
from app.schemas.user_schema import UserOut


class PostRespository(BaseRepository):

    def __init__(self, db: Session, current_user: UserOut):
        self.db = db
        self.current_user = current_user

    def find_by_id(self, id: int):
        post = self.db.query(PostModel).filter(PostModel.id == id).first()
        if not post:
            raise Exceptions.exception_404()
        if not post.owner_id == self.current_user.id:
            raise Exceptions.exception_404()
        return post
    
    def find_all(self):
        posts = self.db.query(PostModel).filter(PostModel.owner_id == self.current_user.id).all()
        return posts
    
    def save(self, new_post: PostCreate, user_id):
        post = PostModel(owner_id = user_id, **dict(new_post))
        self.db.add(post)
        self.db.commit()
        self.db.refresh(post)

        return post

    def delete(self, id: int):
        post = self.db.query(PostModel).filter(PostModel.id == id, PostModel.owner_id == self.current_user.id)
        if not post.first():
            raise Exceptions.exception_404()
        post.delete(synchronize_session=False)
        self.db.commit()
        return
    
    def update(self, id: int, upd_post: PostCreate):
        post = self.db.query(PostModel).filter(PostModel.id == id, PostModel.owner_id == self.current_user.id)
        if not post.first():
            raise Exceptions.exception_404()
        
        post.update(dict(upd_post))
        self.db.commit()
        return post.first()
    
    