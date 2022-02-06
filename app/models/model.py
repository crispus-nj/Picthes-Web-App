from app import db
from datetime import datetime

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(200))
    pitches = db.relationship('Pitches', backref='user', lazy=True)

class Pitches(db.Model):

    __tablename__ = 'pictches'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(40), nullable=False,)
    content = db.Column(db.String(200), nullable=False,)
    date_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)