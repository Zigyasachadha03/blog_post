import app.schemas.user_schema as user_schema
from app.schemas.vote_schema import Vote
from sqlalchemy.orm import Session
from app.repositories.vote_repo import VoteRepository

class VoteService:
    def __init__(self, db: Session, current_user: user_schema.UserOut):
        self.repository = VoteRepository(db, current_user)

    def create_vote(self, new_vote: Vote):
        return self.repository.save(new_vote)