import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import DevConfig
from flask_migrate import Migrate
from flask_login import LoginManager

# instance of the application
app = Flask(__name__)

# dev configurations
app.config.from_object(DevConfig)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

# Database configurations
app.config['SQLALCHEMY_DATABASE_URI'] 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
Migrate(app, db)

# loggin configurations
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from app import views