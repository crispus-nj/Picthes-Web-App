from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError, Length
from .models import model

User = model.User

class RegisterForm(FlaskForm):
    '''
    Register form used for creating custom registration form on the client side.
    '''
    username = StringField("Username", validators=[DataRequired()])
    email = EmailField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=6, max=50)])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        '''
        validate_username function for checking if the username is available for selection or it has already been taken
        '''
        user = User.query.filter_by(username = username.data).first()
        if user:
            raise ValidationError('Username already taken!')

        

    def validate_email(self, email):
        '''
        validate_email function for checking if the email is available for selection or it has already been taken
        '''
        user = User.query.filter_by(email = email.data).first()
        if user:
            raise  ValidationError("Email already take!")

class LoginForm(FlaskForm):
    '''
    Register form used for creating custom login form on the client side.
    '''
    email = EmailField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(),Length(min=6, max=50)])
    submit = SubmitField('Sign In')
