from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField, RadioField
from wtforms.validators import Length

# Define edit user profile form
class EditProfileForm(FlaskForm):
    about_me = TextAreaField('About Me', validators=[Length(min=0, max=180)])
    avatar = RadioField('Choose Your Avatar Color', choices=[
        ('1', 'Orange'), 
        ('2', 'Green'), 
        ('3', 'Blue'),
        ('4', 'Purple')])
    submit = SubmitField('Submit')

