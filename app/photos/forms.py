from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, FileField, SelectField
from wtforms.validators import DataRequired, Length
from app.models import Category

# Photo upload form setup
class UploadPhoto(FlaskForm):
    title = StringField(
        'Photo Title', 
        validators=[DataRequired(
            message="Please enter your username."),
            Length(max=25)])
    description = TextAreaField(
        'Description of your photo', 
        validators=[DataRequired(
            message="Please enter a description."),
            Length(min=0, max=180)])
    category_name = SelectField('Choose Category',
        choices=[
            (category.category_name) 
            for category in Category.objects],
        validators=[DataRequired(
            message="Please choose a category.")])
    # url = FileField('Photo')
    submit = SubmitField('Add Photo')


class EditPhotoForm(FlaskForm):
    title = StringField(
        'Photo Title', 
        validators=[DataRequired(
            message="Please enter a valid title."),
            Length(max=25)])
    description = TextAreaField(
        'Description of your photo', 
        validators=[DataRequired(
            message="Please enter a description."),
            Length(min=0, max=180)])
    category = SelectField('Choose Category',
        choices=[
            (category.category_name) 
            for category in Category.objects],
        validators=[DataRequired(
            message="Please choose a category.")])
    submit = SubmitField('Submit')


class AddComment(FlaskForm):
    comment_text = TextAreaField(
        validators=[
            DataRequired('Please add text to submit a comment.'), 
            Length(min=2, max=200)])
    submit = SubmitField('Add Comment')
