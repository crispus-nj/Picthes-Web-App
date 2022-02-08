import os
class Config:
    pass
class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')
class DevConfig(Config):
    DEBUG = True