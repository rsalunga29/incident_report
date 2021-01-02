from fastapi import APIRouter, Depends

from src.auth.views import auth_router, user_router

api_router = APIRouter()

api_router.include_router(auth_router, prefix='/auth', tags=['auth'])
api_router.include_router(user_router, prefix='/users', tags=['users'])
