from starlette.config import Config
from starlette.datastructures import Secret

config = Config('.env')

# Database
DATABASE_HOSTNAME = config('DATABASE_HOSTNAME', default='localhost')
DATABASE_CREDENTIALS = config('DATABASE_CREDENTIALS', cast=Secret)
DATABASE_NAME = config('DATABASE_NAME', default='incident_report')
DATABASE_PORT = config('DATABASE_PORT', default='3306')
SQLALCHEMY_DATABASE_URI = f'mysql://{DATABASE_CREDENTIALS}@{DATABASE_HOSTNAME}:{DATABASE_PORT}/{DATABASE_NAME}'
