from flask_wtf import FlaskForm
from wtforms import (StringField, PasswordField, BooleanField,
                     SubmitField, TextAreaField, RadioField)
from wtforms.validators import DataRequired, Email, EqualTo, Length, Regexp


# Define login form structure & validation
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[
        DataRequired(message="Please enter your username.")])
    password = PasswordField('Password', validators=[
        DataRequired(message="Please enter your password.")])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


# Define registration form structure & validation
class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[
        DataRequired(message="Please enter your desired username."),
        Regexp("^[a-zA-Z0-9]+$",
               message="Can only use letters and numbers, with no spaces.")])
    email = StringField('Email Address', validators=[
        DataRequired(message="Please enter your email address."),
        Email(message="Please enter a vaild email address.")])
    first_name = StringField('First Name', validators=[
        DataRequired(message="Please enter your first name.")])
    last_name = StringField('Last Name', validators=[
        DataRequired(message="Please enter your last name.")])
    about_me = TextAreaField('About Me', validators=[
        Length(min=0, max=180,
               message="About me can only be 180 characters long.")])
    password = PasswordField('Password', validators=[
        DataRequired(message="Please enter your password.")])
    password2 = PasswordField('Confirm Password', validators=[
        DataRequired(message="Please re-enter your password."),
        EqualTo('password', message="Your passwords do not match!")])
    avatar = RadioField('Choose Your Avatar Color',
                        choices=[
                            ('1', 'Red'),
                            ('2', 'Orange'),
                            ('3', 'Teal'),
                            ('4', 'Navy')],
                        default="1",
                        validators=[DataRequired()])
    submit = SubmitField('Register')

    """
    If DataRequired does not have any arguments passed,
    for example message, the following error is returned
    This prevents the application from running
    TypeError: __init__() got an unexpected keyword argument 'valdiators'
    """
