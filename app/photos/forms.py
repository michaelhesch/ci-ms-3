from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField, ValidationError
from wtforms.validators import DataRequired, Length

# Photo upload form
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
    submit = SubmitField('Add Photo')

# Photo editing form
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
    submit = SubmitField('Submit')

# Photo comment form
class AddComment(FlaskForm):
    comment_text = TextAreaField(
        validators=[
            DataRequired('Please add text to submit a comment.'), 
            Length(min=2, max=200)])
    submit = SubmitField('Add Comment')
    
    def validate_comment(form, comment_text):
        if len(comment_text.data) > 200:
            raise ValidationError('Comment must be less than 200 characters')

# Photo edit comment form
class EditComment(FlaskForm):
    comment_text = TextAreaField('Edit Comment', 
        validators=[
            DataRequired('Comment cannot be blank!'), 
            Length(min=2, max=200)])
    submit = SubmitField('Save Changes')

    def validate_comment(form, comment_text):
        if len(comment_text.data) > 200:
            raise ValidationError('Comment must be less than 200 characters')

