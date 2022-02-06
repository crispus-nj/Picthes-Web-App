import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import DevConfig

# instance of the application
app = Flask(__name__)

# dev configurations
app.config.from_object(DevConfig)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

# Database configurations
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
# print(app.config['SQLALCHEMY_DATABASE_URI'])

from app import views