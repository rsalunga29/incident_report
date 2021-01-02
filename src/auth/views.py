from fastapi import APIRouter, Depends, Request, HTTPException, Query
from sqlalchemy.orm import Session

from src.deps import get_db

from .schemas import UserRegister
from .models import Users
from .service import create

auth_router = APIRouter()
user_router = APIRouter()


@auth_router.post('/login')
def login():
    return {'auth': 'views_login_route'}


@auth_router.post('/register')
def register(user_request: UserRegister,
             db_session: Session = Depends(get_db)):
    """Registers a new user

    Args:
        user_request (UserRegister): Schema created using Pydantic
        db_session (Session, optional): The Database session. Defaults to Depends(get_db).

    Returns:
        [type]: [description]
    """
    user = create(db_session=db_session, user_details=user_request)

    return user


@auth_router.post('/logout')
def logout():
    return {'auth': 'views_logout_route'}


@user_router.get('/')
def get_users(db_session: Session = Depends(get_db)):
    return {'user': 'views_get_users_route'}