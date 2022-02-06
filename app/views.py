from app import app
from flask import render_template, redirect, url_for
from .forms import RegisterForm, LoginForm

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/register', methods=['POST', 'GET'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        return ""
    return render_template('register.html', form=form)

@app.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect(url_for('homepage'))
    return render_template('login.html', form=form)
