from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import DevConfig

# instance of the application
app = Flask(__name__)

# dev configurations
app.config.from_object(DevConfig)

# Database configurations
app.config['SQLALCHEMY_DATABASE_URI']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from app import views