from app import db
from flask import render_template, flash, redirect, url_for, request, current_app
from flask_login import current_user, login_required
# from app.photos.forms import 
from app.models import User, Photo
from app.photos import bp


@bp.route('/feed')
def photo_feed():
    photos = list(Photo.objects)
    print(photos)
    
    return render_template("photos/feed.html", photos=photos)