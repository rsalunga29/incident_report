from fastapi import FastAPI
from starlette.applications import Starlette

from .api import api_router

# we create the ASGI for the app
app = Starlette()

# we create the ASGI for the frontend
frontend = Starlette()

# we create the Web API framework
api = FastAPI()

api.include_router(api_router, prefix='/v1')

app.mount('/api', app=api)
app.mount('/', app=frontend)
