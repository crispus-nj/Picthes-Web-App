class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:pitches@localhost/pitches'
class ProdConfig(Config):
    pass
class DebConfig(Config):
    DEBUG = True