import bcrypt
from pydantic import BaseModel, validator


class UserBase(BaseModel):
    name: str
    email: str

    @validator('email')
    def email_required(cls, v):
        if not v:
            raise ValueError('Must not be empty string and must be an email')

        return v


class UserRegister(UserBase):
    password: str

    @validator('password', pre=True, always=True)
    def password_required(cls, v):
        return hash_password(v)


class UserLogin(UserBase):
    password: str

    @validator('password')
    def password_required(cls, v):
        if not v:
            raise ValueError('Must not be empty string')

        return v


def hash_password(password: str) -> str:
    password = bytes(password, 'utf-8')
    salt = bcrypt.gensalt()

    return bcrypt.hashpw(password, salt)
