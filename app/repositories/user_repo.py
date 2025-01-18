from app.repositories import BaseRepository
from sqlalchemy.orm import Session
from app.schemas.user_schema import UserCreate
from app.models import UserModel
from app.utils import hash_password
from app.exception import Exceptions

class UserRepository(BaseRepository):
    def __init__(self, db: Session):
        self.db = db

    def find_by_id(self, id: int):
        user = self.db.query(UserModel).filter(UserModel.id == id).first()
        if not user:
            raise Exceptions.exception_404()
        return user
    
    def find_all(self):
        users = self.db.query(UserModel).all()
        return users
    
    def save(self, new_user: UserCreate):
        if not new_user.password:
            raise Exceptions.exception_400()
        new_user.password = hash_password(new_user.password) 
        user = UserModel(**dict(new_user))
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def delete(self, id: int):
        user = self.db.query(UserModel).filter(UserModel.id == id)
        if not user.first():
            raise Exceptions.exception_404()
        user.delete(synchronize_session=False)
        return
    
    def update(self, id: int, upd_user: UserCreate):
        user = self.db.query(UserModel).filter(UserModel.id == id)

        if not user.first():
            raise Exceptions.exception_404()
        
        user.update(dict(upd_user))
        self.db.commit()
        return user.first()
    

    