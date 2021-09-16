import os
from datetime import timedelta
import cloudinary


class Config(object):
    # Import flask secret key environment variable
    SECRET_KEY = os.environ.get("SECRET_KEY")
    # Configure LoginManager to invalidate sessions after 12 hours
    PERMANENT_SESSION_LIFETIME = timedelta(hours=12)
    # Import cloudinary configuration environment variables
    cloudinary.config(
        cloud_name = os.getenv('CLOUD_NAME'), 
        api_key = os.getenv('API_KEY'), 
        api_secret = os.getenv('API_SECRET'))

    # Import MongoDB configuration environment variables
    MONGODB_SETTINGS = {
        'db': os.environ.get("MONGO_DB"),
        'host': os.environ.get("MONGO_URI")
    }