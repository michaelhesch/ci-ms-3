from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField
from wtforms.validators import Length
# from wtforms.widgets.core import TextArea
# from app.models import User

# Define edit user profile form
class EditProfileForm(FlaskForm):
    about_me = TextAreaField('About Me', validators=[Length(min=0, max=180)])
    submit = SubmitField('Submit')
