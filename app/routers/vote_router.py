from fastapi import APIRouter, Depends
from app.database import get_db
from sqlalchemy.orm import Session
from app.schemas.vote_schema import Vote
import app.schemas.user_schema as user_schema
from app.services import VoteService, PostService
from app.oauth2 import get_current_user

vote_api_router = APIRouter(
    tags = ['Votes'],
    prefix='/votes'
)


@vote_api_router.post('/')
def create_vote(new_vote: Vote, db: Session = Depends(get_db), current_user: user_schema.UserOut= Depends(get_current_user)):
    vote_service = VoteService(db, current_user)
    return vote_service.create_vote(new_vote)