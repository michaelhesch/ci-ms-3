import datetime
from mongoengine.errors import ValidationError
from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

# User class setup
class User(db.Document, UserMixin):
    username = db.StringField(max_length=14, unique=True, required=True)
    first_name = db.StringField(max_length=25, required=True)
    last_name = db.StringField(max_length=35, required=True)
    email = db.EmailField(max_length=50, unique=True, required=True)
    about_me = db.StringField(max_length=180)
    password_hash = db.StringField(required=True)

    # Password hashing function
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    # Check password vs hashed password function
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    # Dunder method to configure how User object is returned when printed
    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"

# Photo category class setup
class Category(db.Document):
    category_name = db.StringField(required=True) 

    # Dunder method to configure how Category object is returned when printed
    def __repr__(self):
        return f"Category('{self.category_name}')"

# Photo class setup
class Photo(db.Document):
    category_name = db.ReferenceField(Category)
    title = db.StringField(max_length=30, unique=True, required=True)
    description = db.StringField(max_length=180)
    user_uploaded_by = db.StringField(max_length=14, required=True)
    user_added_datetime = db.DateTimeField(default=datetime.datetime.utcnow)
    url = db.URLField()
    likes = db.IntField(default=0)
    liked_by_user = db.ListField(db.ReferenceField(User))

    # Dunder method to configure how Photo object is returned when printed
    def __repr__(self):
        return f"Photo('{self.title}', '{self.category_name}', '{self.user_uploaded_by}')"

    # TODO implement folders for each user's photos in cloudinary
    """def upload_photo(self, user, new_photo):
        user_folder = f"ooo/{user}"
        upload_result = uploader.upload(new_photo, user_folder=user_folder)"""


# Comment class setup
class Comment(db.Document):
    user_comment_by = db.ReferenceField(User)
    user_comment_datetime = db.DateTimeField(default=datetime.datetime.utcnow)
    photo_commented_on = db.ReferenceField(Photo)
    comment_text = db.StringField(min_length=2, max_length=200, required=True)
    likes = db.IntField(default=0)
    liked_by_user = db.ListField(db.ReferenceField(User))

    # Dunder method to configure how Comment object is returned when printed
    def __repr__(self):
        return f"Comment('{self.user_comment_by}', '{self.photo_commented_on}', '{self.comment_text}')"


# Flask login manager user loader - gets current user ID from DB
# User model above inherits from UserMixin class to provide required 
# validation attributes & methods to login manager
@login.user_loader
def load_user(id):
    return User.objects.get(pk=id) # TODO: Confirm why only pk=id works as this argument?
    """
    If pk=id not passed in, this is the error returned by mongoengine:
    This prevents the application from running
    mongoengine.errors.InvalidQueryError: Not a query object: 6133f4f96f1e2846d63bf052. Did you intend to use key=value?
    """
