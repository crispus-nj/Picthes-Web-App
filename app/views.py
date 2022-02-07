from app import app, db
from flask import render_template, redirect, url_for, flash
from .forms import RegisterForm, LoginForm, PitchesForm, CommentForm
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_required, login_user, logout_user, current_user
from .models import model

User = model.User
Picthes = model.Pitches
# Comment = model.Comments

@app.route('/comment',  methods=['POST', 'GET'])
def post_comment():

    pitches = Picthes.query.get_or_404()
    form = CommentForm() 

    if form.validate_on_submit():
        return redirect(url_for('homepage'))

    return render_template('comment.html', form=form)

@app.route('/', methods=['POST', 'GET'])
def homepage():
    db.create_all()
    pitch = Picthes.query.all()
    # form = CommentForm() 
    # if form.validate_on_submit():
    #     return redirect(url_for('homepage'))
    return render_template('index.html', pitch=pitch)

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
        return redirect(url_for('login'))

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


@app.route('/account-info')
@login_required
def account():
    return render_template('account.html')

@app.route('/new-pitch', methods=['POST', 'GET'])
@login_required
def new_pitch():
    form = PitchesForm()
    if form.validate_on_submit():
        pitch = Picthes(title=form.title.data,
                        content=form.content.data,
                        user = current_user
                        )
        db.session.add(pitch)
        db.session.commit()
        flash('Pitch created successfully!', 'success')
        return redirect(url_for('homepage'))

    return render_template('new_pitch.html', form=form)





@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('homepage'))