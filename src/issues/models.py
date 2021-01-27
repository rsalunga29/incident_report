from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, text
from pydantic import BaseModel, validator

from src.database import Base


# SQLAlchemy Models
class Issues(Base):
    __tablename__ = 'issues'
