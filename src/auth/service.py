from typing import Optional

from .models import Users
from .schemas import UserRegister


def check_password(password: str) -> bool:
    pass


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
