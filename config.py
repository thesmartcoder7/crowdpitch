import os

class Config():
    DEBUG = os.getenv('DEBUG')



print(Config.DEBUG)