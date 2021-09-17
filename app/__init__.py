from flask import Flask
from flask_mongoengine import MongoEngine
from flask_login import LoginManager
from config import Config

# Initialize MongoEngine
db = MongoEngine()
# Initialize LoginManager
login = LoginManager()
# Select strong mode for session cookie protection
login.session_protection = 'strong'
login.login_view = 'auth.login'
login.login_message = 'You must be logged in to do that!'


def create_app(config_class=Config):
    # Create Flask app instance with Config vars
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize MongoEngine and LoginManager instances
    db.init_app(app)
    login.init_app(app)

    # Register blueprints from each package
    from app.errors import bp as errors_bp
    app.register_blueprint(errors_bp)

    # Note: if url_prefix is included for main route,
    # '/index' and '/' endpoints will not work
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    from app.auth import bp as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

    from app.photos import bp as photo_bp
    app.register_blueprint(photo_bp, url_prefix='/photos')

    return app
