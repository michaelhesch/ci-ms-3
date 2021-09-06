import os
import cloudinary
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config(object):
    # Import flask secret key environment variable
    SECRET_KEY = os.environ.get("SECRET_KEY")

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