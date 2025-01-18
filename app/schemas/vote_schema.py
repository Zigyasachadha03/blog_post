from pydantic import BaseModel

class Vote(BaseModel):
    post_id: int
    vote_directory: bool = True


# class VoteOut(BaseModel):
#     post_id: int
#     vote_directory: bool

#     class Config:
#         from_attributes = True