import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
class Config():
    DEBUG = os.getenv('DEBUG')
    SECRET_KEY = os.getenv('SECRET_KEY')
    DATABASE_URL = os.getenv('DATABASE_URL')
    EMAIL = os.getenv('EMAIL')
    PASSWORD = os.getenv('PASSWORD')
    SMPT_NAME = os.getenv('SMPT_NAME')


class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    if SQLALCHEMY_DATABASE_URI and SQLALCHEMY_DATABASE_URI.startswith("postgres://"):
        SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.replace("postgres://", "postgresql://", 1)
