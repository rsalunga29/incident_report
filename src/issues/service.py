from typing import Optional

from .models import Issues


def get_all_users(db_session) -> Optional[Issues]:
    return db_session.query(Issues).all()


def get_by_id(db_session, issue_id: int) -> Optional[Issues]:
    return db_session.query(Issues).filter(Issues.id == issue_id).one_or_none()


def get_by_ref_number(db_session, ref_number: str) -> Optional[Issues]:
    return db_session.query(Issues).filter(
        Issues.ref_number == ref_number).one_or_none()


def get_assigned_issues(db_session, assignee_id: int) -> Optional[Issues]:
    return db_session.query(Issues).filter(
        Issues.assignee_id == assignee_id).all()


def create(db_sesion, issue_details) -> Issues:
    pass
