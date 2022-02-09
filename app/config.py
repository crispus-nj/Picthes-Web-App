import os
class Config:
    pass
class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI =  os.environ['SQLALCHEMY_DATABASE_URI']
class DevConfig(Config):
    DEBUG = False
    # 'postgresql+psycopg2://moringa:blog@localhost:5433/pitches'