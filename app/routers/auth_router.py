from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
import app.schemas.login_schema as schema
from app.models import UserModel
from app.exception import Exceptions
from app.utils import verify_password
from app.oauth2 import create_token
from fastapi.security import OAuth2PasswordRequestForm


auth_api_router = APIRouter(
    tags = ['Login'],
    prefix= '/login'
)




@auth_api_router.post('/', response_model=schema.Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(),db: Session = Depends(get_db), ):
    user = db.query(UserModel).filter(UserModel.username == form_data.username).first()
    if not user:
        raise Exceptions.exception_404()
    verify = verify_password(form_data.password, user.password)
    if not verify:
        raise Exceptions.exception_404("Password Not Found")
    data = {'user_id': user.id, 'username': user.username}
    token = create_token(data)
    return schema.Token(access_token=token)