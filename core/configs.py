from typing import ClassVar
from pydantic_settings import BaseSettings
from configparser import ConfigParser
from sqlalchemy.ext.declarative import declarative_base


config = ConfigParser()
config.read('./core/.env')

user: str = config['DATABASE']['user']
passwd: str = config['DATABASE']['passwd']
db: str = config['DATABASE']['db']
host: str = config['DATABASE']['host']
port: str = config['DATABASE']['port']
jwt_secret: str = config['DATABASE']['JWT_SECRET']


class Settings(BaseSettings):

    API_V1_STR: str = '/api/v1'
    DB_URL: str = f'postgresql+asyncpg://{user}:{passwd}@{host}:{port}/{db}'
    DBBaseModel: ClassVar = declarative_base()

    '''
        Código para gerar a JWT secret

        import secrets

        token: str = secrets.token_urlsafe(32)

    '''

    JWT_SECRET: str = jwt_secret

    ALGORITHM: str = 'HS256'

    ACESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7

    class Config:
        case_sensitive = True


settings = Settings()
