import os
import cloudinary

class Config(object):
    # MONGO_DBNAME = os.environ.get("MONGO_DBNAME")
    # MONGO_URI = os.environ.get("MONGO_URI")
    # Import flask secret key
    SECRET_KEY = os.environ.get("SECRET_KEY")

    cloudinary.config(
        cloud_name = os.getenv('CLOUD_NAME'), 
        api_key = os.getenv('API_KEY'), 
        api_secret = os.getenv('API_SECRET'))

    MONGODB_SETTINGS = {
        'db': os.environ.get("MONGO_DB"),
        'host': os.environ.get("MONGO_URI")
    }