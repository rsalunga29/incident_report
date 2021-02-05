from fastapi import HTTPException
from starlette.requests import Request
from starlette.status import HTTP_401_UNAUTHORIZED
from jose import jwt
from typing import Optional

from .models import Users, UserRegister

from src.config import JWT_ALGORITHM, JWT_SECRET


def get_current_user(request: Request) -> Users:
    """Attempts to get the current logged in user. Raises an exception if User is not recognized."""
    if request.headers.get('authorization'):
        token = request.headers.get('authorization').split()
        user = jwt.decode(token[1], JWT_SECRET, algorithms=JWT_ALGORITHM)

        return user
    else:
        raise HTTPException(status_code=HTTP_401_UNAUTHORIZED, detail="Could not validate credentials")


def get_all_users(db_session) -> Optional[Users]:
    return db_session.query(Users).all()


def get_by_id(db_session, user_id: int) -> Optional[Users]:
    return db_session.query(Users).filter(Users.id == user_id).one_or_none()


def get_by_email(db_session, email: str) -> Optional[Users]:
    return db_session.query(Users).filter(Users.email == email).one_or_none()


def create(db_session, user_details: UserRegister) -> Users:
    # pydantic forces a string password, but we really want bytes
    password = bytes(user_details.password, 'utf-8')
    user = Users(**user_details.dict(exclude={'password'}), password=password)
    db_session.add(user)
    db_session.commit()

    return user
