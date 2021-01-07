from fastapi import APIRouter, Depends, Request, HTTPException, Query
from sqlalchemy.orm import Session

from src.deps import get_db

from .models import Users, UserRegister, UserLogin
from .service import create, get_by_email

auth_router = APIRouter()
user_router = APIRouter()


@auth_router.post('/login')
def login(user_request: UserLogin, db_session: Session = Depends(get_db)):
    """[summary]

    Args:
        user_request (UserLogin): Schema created using Pydantic
        db_session (Session, optional): The Database session. Defaults to Depends(get_db).
    """
    user = get_by_email(user_request.email)

    if user and user.check_password(user_request.password):
        return {'token': user.token}

    raise HTTPException(status_code=401, detail='Invalid email or password')


@auth_router.post('/register')
def register(user_request: UserRegister,
             db_session: Session = Depends(get_db)):
    """Registers a new user

    Args:
        user_request (UserRegister): Schema created using Pydantic
        db_session (Session, optional): The Database session. Defaults to Depends(get_db).
    """
    user = create(db_session=db_session, user_details=user_request)

    return user


@auth_router.post('/logout')
def logout():
    return {'auth': 'views_logout_route'}


@user_router.get('/')
def get_users(db_session: Session = Depends(get_db)):
    return {'user': 'views_get_users_route'}