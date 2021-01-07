from starlette.config import Config
from starlette.datastructures import Secret

config = Config('.env')

# Database
DATABASE_HOSTNAME = config('DATABASE_HOSTNAME', default='localhost')
DATABASE_CREDENTIALS = config('DATABASE_CREDENTIALS', cast=Secret)
DATABASE_NAME = config('DATABASE_NAME', default='incident_report')
DATABASE_PORT = config('DATABASE_PORT', default='3306')
SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{DATABASE_CREDENTIALS}@{DATABASE_HOSTNAME}:{DATABASE_PORT}/{DATABASE_NAME}'

# JWT Settings
JWT_EXPIRATION = config('JWT_EXPIRATION', cast=int, default=86400)
JWT_ALGORITHM = config('JWT_ALGORITHM', default='HS256')
JWT_SECRET = config('JWT_SECRET', default=None)
