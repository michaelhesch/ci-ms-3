from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class User(UserMixin, db.Document):
    username = db.StringField(max_length=14, unique=True, required=True)
    first_name = db.StringField(max_length=25, required=True)
    last_name = db.StringField(max_length=35, required=True)
    email = db.EmailField(max_length=100, unique=True, required=True)
    password_hash = db.StringField(required=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)


# Flask login user loader - gets user ID from DB
@login.user_loader
def load_user(id):
    return User.objects.get(pk=id) # TODO: Confirm why only pk=id works as this argument?
    """
    If pk=id not passed in, this is the error returned by mongoengine:
    This prevents the application from running
    mongoengine.errors.InvalidQueryError: Not a query object: 6133f4f96f1e2846d63bf052. Did you intend to use key=value?
    """
