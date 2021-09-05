from flask import Flask
from flask_mongoengine import MongoEngine
from flask_login import LoginManager
from config import Config

# Create Flask app and import config
app = Flask(__name__)
app.config.from_object(Config)

# Initialize MongoEngine
db = MongoEngine(app)
# Initialize LoginManager
login = LoginManager(app)
# Select strong mode for session cookie protection
login.session_protection = "strong"
login.login_view = 'login'

from app import routes
