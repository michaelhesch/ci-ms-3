import os
import cloudinary
import cloudinary.uploader
import cloudinary.api
from datetime import datetime
from dotenv import load_dotenv
from flask_pymongo import PyMongo
from flask import (
    Flask, render_template, flash, jsonify,
    redirect, request, session, url_for)
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, login_required, current_user
# Import environment variables for local development
if os.path.exists("env.py"):
    import env

# Define Flask app
app = Flask(__name__)

# Initialize login manager
#login_manager = LoginManager()
#login_manager.init_app(app)


#@login_manager.user_loader
#def load_user(user):
#    if session["user"]:
#        return mongo.db.users.find_one(
#            {"user_name": request.form.get("username").lower()})

load_dotenv()

# Import environment variables for MongoDB
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

# Define mongoDB for current instance of app
mongo = PyMongo(app)

# Flask endpoints
@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # Check DB for duplicate username
        existing_user = mongo.db.users.find_one(
            {"user_name": request.form.get("username").lower()})
        # Consume user form input for data validation checks
        fname = request.form.get("firstName")
        lname = request.form.get("lastName")
        username = request.form.get("username")
        pass1 = request.form.get("pass1")
        pass2 = request.form.get("pass2")
        email = request.form.get("email")

        # New user data quality checks before sending to DB
        if existing_user:
            flash("Username already exists, please try another username.")
            return redirect(url_for("register"))
        elif len(username) < 4:
            flash("Username must be longer than four characters")
            return redirect(url_for("register"))
        elif len(fname) < 3:
            flash("First name must be at least three characters")
            return redirect(url_for("register"))
        elif len(lname) < 3:
            flash("Last name must be at least three characters")
            return redirect(url_for("register"))
        elif pass1 != pass2:
            flash("Passwords do not match, please try again.")
            return redirect(url_for("register"))
        elif len(pass1) < 6:
            flash("Password must be at least 6 characters, please try again")
            return redirect(url_for("register"))
        elif len(email) < 4:
            flash("Email must be greater than four characters")
            return redirect(url_for("register"))
        else:
            register = {
                "user_name": request.form.get("username").lower(),
                "password": generate_password_hash(request.form.get("pass1")),
                "first_name": request.form.get("firstName").lower(),
                "last_name": request.form.get("lastName").lower(),
                "email": request.form.get("email")
            }
            mongo.db.users.insert_one(register)

        # Create session for new user
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Check DB for existing user
        existing_user = mongo.db.users.find_one(
            {"user_name": request.form.get("username").lower()})
        
        if existing_user:
            # Check hashed pass from DB matches user input
            if check_password_hash(
                existing_user["password"], request.form.get("pass1")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome back, {}".format(
                        request.form.get("username")))
                    return redirect(
                        url_for("profile", username=session["user"]))
            else:
                # Bad password response
                flash("Incorrect login details, please try again.")
                return redirect(url_for("login"))

        else:
            # Bad username response
            flash("Incorrect login details, please try again.")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
#@login_required
def profile(username):
    # Take current session user's username and pass to profile page
    username = mongo.db.users.find_one(
        {"user_name": session["user"]})["user_name"]

    photos = list(mongo.db.photos.find())
    # Check session cookie is correct for user before returning profile
    if session["user"]:
        return render_template("profile.html", username=username, photos=photos)

    return redirect(url_for("login"))


@app.route("/logout")
#@login_required
def logout():
    flash("You have been logged out.")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/photo/<photo>")
def photo(photo):
    photo =  mongo.db.photos.find_one({"_id": ObjectId(photo)})

    username = mongo.db.users.find_one(
        {"user_name": session["user"]})["user_name"]
    return render_template("photo.html", username=username, photo=photo)


@app.route("/add_photo", methods=["GET", "POST"])
def add_photo():
    categories = mongo.db.categories.find().sort("category_name", 1)

    return render_template("add_photo.html", categories=categories)


@app.route("/upload", methods=["POST"])
def upload_photo():
# Cloudinary image upload
    cloudinary.config(
        cloud_name = os.getenv('CLOUD_NAME'), 
        api_key = os.getenv('API_KEY'), 
        api_secret = os.getenv('API_SECRET'))

    upload_result = None

    if request.method == 'POST':
        file_to_upload = request.files['file']

        if file_to_upload:
            upload_result = cloudinary.uploader.upload(file_to_upload)
            jsonify(upload_result)
            # Converts form data into dictionary before inserting to DB
            photo = {
                "category_name": request.form.get("category_name"),
                "title": request.form.get("title"),
                "description": request.form.get("description"),
                "user_uploaded_by": session["user"],
                "user_added_datetime": datetime.now(),
                "url": "",
                "num_likes": 0
            }
            mongo.db.photos.insert_one(photo)
            flash("Photo added!")
        return redirect(url_for("profile", username=session["user"]))

    else:
        flash("Photo not uploaded, please try again.")


@app.route("/feed")
def photo_feed():
    photos = list(mongo.db.photos.find())
    return render_template("feed.html", photos=photos)


# Create app
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
    port=int(os.environ.get("PORT")),
    debug=True) # UPDATE TO DEBUG = FALSE BEFORE DEPLOYMENT
