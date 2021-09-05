from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo, Length
# from wtforms.widgets.core import TextArea
from app.models import User

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
        DataRequired(message="Please enter your username.")])
    email = StringField('Email', validators=[
        DataRequired(message="Please enter your email."), 
        Email()])
    first_name = StringField('first_name', validators=[
        DataRequired(message="Please enter your first name.")])
    last_name = StringField('last_name', validators=[
        DataRequired(message="Please enter your last name.")])
    about_me = TextAreaField('About Me', validators=[
        Length(min=0, max=180)])
    password = PasswordField('Password', validators=[
        DataRequired(message="Please enter your password.")])
    password2 = PasswordField('RepeatPassword', validators=[
        DataRequired(message="Please re-enter your password."), 
        EqualTo('password')])
    submit = SubmitField('Register')

    """
    If DataRequired does not have any arguments passed, for example message, the following error is returned
    This prevents the application from running
    TypeError: __init__() got an unexpected keyword argument 'valdiators'
    """

    # Check for duplicate username in db (first match)
    def check_username(self, username):
        duplicate = User.objects(username=username.data).first()
        if duplicate is not None:
            raise ValidationError(
                'Invalid username, please try a new username.')

    # Check for duplicate email in db (first match)
    def check_email(self, email):
        duplicate = User.objects(email=email.data).first()
        if duplicate is not None:
            raise ValidationError(
                'Invalid username, please try a new username.')
