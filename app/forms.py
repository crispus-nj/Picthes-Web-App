from ast import Pass
from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError, Length

class RegisterForm(FlaskForm):
    '''
    Register form used for creating custom registration form on the client side.
    '''
    username = StringField("Username", validators=[DataRequired()])
    email = EmailField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=6, max=50)])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    # def validate_username(self):
    #     '''
    #     validate_username function for checking if the username is available for selection or it has already been taken
    #     '''
    #     pass

    # def validate_email(self):
    #     '''
    #     validate_email function for checking if the email is available for selection or it has already been taken
    #     '''
    #     pass

class LoginForm(FlaskForm):
    '''
    Register form used for creating custom login form on the client side.
    '''
    email = EmailField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField('Sign In')
