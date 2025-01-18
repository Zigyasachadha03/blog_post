from app.repositories import UserRepository
from sqlalchemy.orm import Session
from app.schemas.user_schema import UserCreate


class UserService:
    def __init__(self, db: Session):
        self.repository = UserRepository(db)

    def get_all(self):
        return self.repository.find_all()
    
    def get_user_by_id(self, id: int):
        return self.repository.find_by_id(id)
    
    def create_user(self, new_user: UserCreate):
        return self.repository.save(new_user)
    
    def delete_user(self, id: int):
        return self.repository.delete(id)
    
    def update_user(self, id: int, upd_user: UserCreate):
        return self.repository.update(id, upd_user)