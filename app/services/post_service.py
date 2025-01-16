from app.repositories import PostRespository
from app.schemas.post_schema import PostCreate
from sqlalchemy.orm import Session

class PostService:
    def __init__(self, db: Session):
        self.repository = PostRespository(db)

    def get_post_by_id(self, id: int):
        return self.repository.find_by_id(id)

    def get_all(self):
        return self.repository.find_all()
    
    def create_post(self, new_post: PostCreate):
        return self.repository.save(new_post)
    
    def delete_post(self, id: int):
        return self.repository.delete(id)
    
    def update_post(self, id: int, upd_post: PostCreate):
        return self.repository.update(id, upd_post)