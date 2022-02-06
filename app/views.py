from app import app, db
from flask import render_template, redirect, url_for, flash
from .forms import RegisterForm, LoginForm
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_required, login_user, logout_user
from .models import model

User = model.User
Picthes = model.Pitches

@app.route('/')
def homepage():
    db.create_all()
    user = User.query.all()
    return render_template('index.html', user=user)

@app.route('/register', methods=['POST', 'GET'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(username = form.username.data, 
                    email = form.email.data, 
                    password = generate_password_hash(form.password.data))
        db.session.add(user)
        db.session.commit()           
        flash('Account created successfull. You can now login!', 'success')           
        return redirect(url_for('homepage'))

    return render_template('register.html', form=form)

@app.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            flash(f'{user.username} logged in successfully', 'success')
            return redirect(url_for('homepage'))
    return render_template('login.html', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('homepage'))