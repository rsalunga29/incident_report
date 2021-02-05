import bcrypt

from datetime import datetime, timedelta
from sqlalchemy import Column, Integer, String, DateTime, Binary, text
from sqlalchemy.orm import backref, relationship
from pydantic import BaseModel, validator
from jose import jwt

from src.database import Base
from src.config import JWT_EXPIRATION, JWT_ALGORITHM, JWT_SECRET


def hash_password(password: str) -> str:
    password = bytes(password, 'utf-8')
    salt = bcrypt.gensalt()

    return bcrypt.hashpw(password, salt)


# SQLAlchemy Models
class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(Binary, nullable=False)
    created_at = Column(DateTime, nullable=False, server_default=text('now()'))

    issues = relationship(
        'Issues',
        primaryjoin='Users.id==Issues.assignee_id',
    )

    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password)

    @property
    def token(self):
        now = datetime.utcnow()
        exp = (now + timedelta(seconds=JWT_EXPIRATION)).timestamp()
        data = {'exp': exp, 'name': self.name, 'email': self.email, 'id': self.id}

        return jwt.encode(data, JWT_SECRET, algorithm=JWT_ALGORITHM)


# Pydantic Models
class UserBase(BaseModel):
    name: str
    email: str

    class Config:
        orm_mode = True
        validate_assignment = True

    @validator('email')
    def email_required(cls, v):
        if not v:
            raise ValueError('Must not be an empty string and must be an email')

        return v


class UserRegister(UserBase):
    password: str

    @validator('password', pre=True, always=True)
    def password_required(cls, v):
        return hash_password(v)


class UserLogin(BaseModel):
    email: str
    password: str

    @validator('email')
    def email_required(cls, v):
        if not v:
            raise ValueError('Must not be an empty string and must be an email')

        return v

    @validator('password')
    def password_required(cls, v):
        if not v:
            raise ValueError('Must not be an empty string')

        return v


class UserRead(UserBase):
    id: int
    created_at: datetime


class AssignedIssues(UserBase):
    issues: list
