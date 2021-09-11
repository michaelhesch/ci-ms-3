from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField, RadioField
from wtforms.validators import Length

# Define edit user profile form
class EditProfileForm(FlaskForm):
    about_me = TextAreaField('About Me', validators=[Length(min=0, max=180)])
    avatar = RadioField('Choose Your Avatar', choices=[('1', 'Description of 1'), ('2', 'Description of 2'), ('3', 'Description of 3')])
    submit = SubmitField('Submit')

