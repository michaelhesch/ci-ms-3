import os
from flask_pymongo import PyMongo
from flask import (
    Flask, render_template, flash, 
    redirect, request, session, url_for)
from bson.objectid import ObjectId
# Import environment variables for local development
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

# Import environment variables for MongoDB
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

@app.route("/")
@app.route("/home")
def home():
    users = mongo.db.users.find()
    return render_template("index.html", users=users)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
    port=int(os.environ.get("PORT")),
    debug=True) # UPDATE TO DEBUG = FALSE BEFORE DEPLOYMENT
