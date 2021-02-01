from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Date, text
from sqlalchemy.orm import relationship
from pydantic import BaseModel, validator

from src.database import Base


# SQLAlchemy Models
class Issues(Base):
    __tablename__ = 'issues'

    id = Column(Integer, primary_key=True, index=True)

    reporter_id = Column(Integer, ForeignKey('users.id', ondelete='cascade'))
    assignee_id = Column(Integer, ForeignKey('users.id', ondelete='cascade'))

    ref_number = Column(String, nullable=False)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    date_discovered = Column(Date, nullable=False)
    created_at = Column(DateTime, nullable=False, server_default=text('now()'))

    # reporter = relationship(
    #     'Users',
    #     # back_populates='issues',
    #     foreign_keys=[reporter_id],
    # )
    # assignee = relationship(
    #     'Users',
    #     # back_populates='issues',
    #     foreign_keys=[assignee_id],
    # )
