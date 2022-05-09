import os
from dotenv import load_dotenv, find_dotenv

class Config():
    DEBUG = os.getenv('DEBUG')
    SECRET_KEY = os.getenv('SECRET_KEY')
