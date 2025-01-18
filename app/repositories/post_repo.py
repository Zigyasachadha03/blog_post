from app.repositories import BaseRepository
from app.models import PostModel, VoteModel
from app.schemas import PostCreate
from app import Exceptions
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.schemas.user_schema import UserOut
from app.schemas.post_schema import PostOut


class PostRespository(BaseRepository):

    def __init__(self, db: Session, current_user: UserOut):
        self.db = db
        self.current_user = current_user

    def find_by_id(self, id: int):
        # post = self.db.query(PostModel).filter(PostModel.id == id).first()
        post_data = self.db.query(PostModel, func.count(VoteModel.post_id).label("votes")).join(
        VoteModel, VoteModel.post_id == PostModel.id, isouter=True).group_by(PostModel.id).filter(PostModel.id == id).first()

        if not post:
            raise Exceptions.exception_404()
        post, votes = post_data
        return PostOut(post=post, votes=votes)
    
    def find_all(self):
        post_data = self.db.query(PostModel, func.count(VoteModel.post_id).label("votes")).join(VoteModel, VoteModel.post_id == PostModel.id, isouter= True).group_by(PostModel.id).all()
        # posts = self.db.query(PostModel).filter(PostModel.owner_id == self.current_user.id).all()
        results = [{PostOut.post:post, PostOut.votes: votes} for post, votes in post_data]
        return results
    
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
    
    