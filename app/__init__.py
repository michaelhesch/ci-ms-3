from flask import Flask
from flask_mongoengine import MongoEngine
from flask_login import LoginManager
from config import Config

# Create Flask app and import config
# app = Flask(__name__)
# app.config.from_object(Config)

# Import errors blueprint
# from app.errors import bp as errors_bp
# Register error handling blueprint with main app
# app.register_blueprint(errors_bp)

# Import authentication blueprint
# from app.auth import bp as auth_bp
# Register authentication blueprint with app
# app.register_blueprint(auth_bp, url_prefix='/auth')

# Initialize MongoEngine
db = MongoEngine()
# Initialize LoginManager
login = LoginManager()
# Select strong mode for session cookie protection
login.session_protection = "strong"
login.login_view = 'login'


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    login.init_app(app)

    from app.errors import bp as errors_bp
    app.register_blueprint(errors_bp)

    from app.auth import bp as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

    return app