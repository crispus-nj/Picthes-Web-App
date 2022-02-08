import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')
class ProdConfig(Config):
    pass
class DevConfig(Config):
    DEBUG = True