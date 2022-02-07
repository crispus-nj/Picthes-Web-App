from xml.etree.ElementTree import Comment
from app import app, db
from flask import render_template, redirect, url_for, flash, request
from .forms import RegisterForm, LoginForm, PitchesForm, CommentForm, UpdateAccountForm
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_required, login_user, logout_user, current_user
from .models import model

User = model.User
Picthes = model.Pitches
Comment = model.Comments

@app.route('/')
def homepage():
    db.create_all()
    pitch = Picthes.query.all()
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


@app.route('/comment/<pitch_id>',  methods=['POST', 'GET'])
@login_required
def post_comment(pitch_id):

    pitches = Picthes.query.get_or_404(pitch_id)
    form = CommentForm() 

    if form.validate_on_submit():
        # pitch = Picthes.query.filter_by(current_user.pitch_id).first()
        comment = Comment(comment = form.comment.data)
        db.session.add(comment)
        db.session.commit()
        print(comment)
        return redirect(url_for('homepage'))

    return render_template('comment.html', title=pitches.title , pitches=pitches,form=form)

@app.route('/account',methods=['POST', 'GET'] )
@login_required
def account_info():

    form = UpdateAccountForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        flash('Username updated successfull!', 'success')
        db.session.commit()
        
    if request.method == 'GET':
        form.username.data = current_user.username

    return render_template('account.html', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('homepage'))