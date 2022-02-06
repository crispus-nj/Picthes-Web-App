from app import app
from flask import render_template
from .forms import RegisterForm, LoginForm

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/register', methods=['POST', 'GET'])
def register():
    form = RegisterForm()
    return render_template('register.html', form=form)

@app.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    return render_template('login.html', form=form)
