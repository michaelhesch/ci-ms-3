from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField, RadioField
from wtforms.validators import Length


# Define edit user profile form
class EditProfileForm(FlaskForm):
    about_me = TextAreaField('About Me', validators=[Length(min=0, max=180)])
    avatar = RadioField('Choose Your Desired Avatar Color', choices=[
        ('1', 'Red'),
        ('2', 'Orange'),
        ('3', 'Teal'),
        ('4', 'Navy')])
    submit = SubmitField('Save Changes')
