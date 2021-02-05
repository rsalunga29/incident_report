from fastapi import APIRouter, Depends
from sqlalchemy.sql.sqltypes import JSON
from starlette.responses import JSONResponse

from src.auth.service import get_current_user
from src.auth.views import auth_router, user_router
from src.issues.views import issues_router

api_router = APIRouter(default_response_class=JSONResponse)
authenticated_api_router = APIRouter()

api_router.include_router(auth_router, prefix='/auth', tags=['auth'])
authenticated_api_router.include_router(user_router, prefix='/users', tags=['users'])
authenticated_api_router.include_router(issues_router, prefix='/issues', tags=['issues'])


@api_router.get('/health', include_in_schema=False)
def healthcheck():
    return {'status': 'ok'}


api_router.include_router(authenticated_api_router, dependencies=[Depends(get_current_user)])
