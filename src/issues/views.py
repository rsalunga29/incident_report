from fastapi import APIRouter, Depends, Request, HTTPException, Query
from sqlalchemy.orm import Session

from src.deps import get_db

from .models import Issues
from .service import create

issues_router = APIRouter()


@issues_router.get('/')
def get_all_issues(db_session: Session = Depends(get_db)):
    """Get all issues posted by all users

    Args:
        db_session (Session, optional): The Database session. Defaults to Depends(get_db).
    """
    pass


@issues_router.post('/create')
def create_issue(db_session: Session = Depends(get_db)):
    issue = create(db_session=db_session, issue_details=[])

    return issue


@issues_router.patch('/update/{issue_id}')
def update_issue(issue_id: int, db_session: Session = Depends(get_db)):
    pass
