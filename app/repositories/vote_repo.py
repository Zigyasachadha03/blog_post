from app.repositories import BaseRepository
from sqlalchemy.orm import Session
import app.schemas.user_schema as user_schema
import app.schemas.vote_schema as schema
from app.models import PostModel, VoteModel
from app.exception import Exceptions


class VoteRepository(BaseRepository):
    def __init__(self, db: Session, current_user: user_schema.UserOut):
        self.db = db
        self.current_user = current_user

    def find_by_id(self, id: int):
        pass
    
    def find_all(self):
        pass
    
    def save(self, new_vote: schema.Vote):   
        post = self.db.query(PostModel).filter(PostModel.id == new_vote.post_id).first()
        if not post:
            raise Exceptions.exception_404()
        user_voted = self.db.query(VoteModel).filter(VoteModel.user_id == self.current_user.id, VoteModel.post_id == new_vote.post_id)
        found_vote = user_voted.first()

        if new_vote.vote_directory:
            if found_vote:
                raise Exceptions.exception_409()
        
            vote = VoteModel(user_id = self.current_user.id, post_id = new_vote.post_id)
            self.db.add(vote)
            self.db.commit()
            self.db.refresh(vote)
            return {"message": "successfully vote added"}
        
        else:
            if not found_vote:
                raise Exceptions.exception_409()
            
            user_voted.delete(synchronize_session = False)
            self.db.commit()
            return {"message": "successfully vote deleted"}

    def delete(self, id: int):
        pass
    
    def update(self):
        pass