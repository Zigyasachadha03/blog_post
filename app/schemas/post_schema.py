from pydantic import BaseModel
from datetime import datetime
from app.schemas import user_schema, vote_schema

class PostBase(BaseModel):
    title: str
    content: str
    published: bool


class PostCreate(PostBase):
    pass

class Post(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: user_schema.UserOut

    class Config:
        from_attributes = True

class PostOut(BaseModel):
    post: Post
    votes: int

    class Config:
        from_attributes = True