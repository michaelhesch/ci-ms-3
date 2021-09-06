import datetime
from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

# User class setup
class User(UserMixin, db.Document):
    username = db.StringField(max_length=14, unique=True, required=True)
    first_name = db.StringField(max_length=25, required=True)
    last_name = db.StringField(max_length=35, required=True)
    email = db.EmailField(max_length=50, unique=True, required=True)
    about_me = db.StringField(max_length=180)
    password_hash = db.StringField(required=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)

# Photo category class setup
class Category(db.Document):
    category_name = db.StringField(required=True) 

    def __repr__(self):
        return "<Category {}".format(self.category_name)

# Photo class setup
class Photo(db.Document):
    category_name = db.ReferenceField(Category)
    title = db.StringField(max_length=30, unique=True, required=True)
    description = db.StringField(max_length=180)
    user_uploaded_by = db.StringField(max_length=14, required=True)
    user_added_datetime = db.DateTimeField(default=datetime.datetime)
    url = db.URLField()
    likes = db.IntField()

    def __repr__(self):
        return '<Photo {}>'.format(self.title)

# Flask login user loader - gets user ID from DB
@login.user_loader
def load_user(id):
    return User.objects.get(pk=id) # TODO: Confirm why only pk=id works as this argument?
    """
    If pk=id not passed in, this is the error returned by mongoengine:
    This prevents the application from running
    mongoengine.errors.InvalidQueryError: Not a query object: 6133f4f96f1e2846d63bf052. Did you intend to use key=value?
    """
