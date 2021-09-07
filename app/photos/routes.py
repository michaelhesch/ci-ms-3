from app import db
from flask import render_template, flash, redirect, url_for, request, current_app
from flask_login import current_user, login_required
# from app.photos.forms import 
from app.models import User, Photo
from app.photos import bp
from app.photos.forms import UploadPhoto
import datetime
from cloudinary import uploader
from bson.objectid import ObjectId


@bp.route('/feed')
def photo_feed():
    photos = list(Photo.objects)
    
    return render_template("photos/feed.html", photos=photos)


@bp.route('/upload', methods=["GET", "POST"])
@login_required
def upload_photo():
    # Create empty result variable for cloudinary upload
    upload_result = None
    # Create instance of UploadPhoto form class
    form = UploadPhoto()
    # Check for post request and form validate on submit
    if request.method == "POST" and form.validate_on_submit():
        # Capture file from form for cloudinary upload
        file_to_upload = request.files['file']
        # If file is found, upload to cloudinary
        if file_to_upload:
            upload_result = uploader.upload(file_to_upload)
        # Populate Photo object to send to mongoDB
        new_photo = Photo(title=form.title.data,
            description=form.description.data,
            user_uploaded_by=current_user.username,
            user_added_datetime=datetime.datetime.utcnow,
            # Select the secure url value from cloudinary response
            url= upload_result["secure_url"])
        # Save to mongodb
        new_photo.save()
        # Flash message to user and return to profile page
        flash("New photo added!")
        return redirect(url_for('main.profile', username=current_user.username))
    
    return render_template('photos/upload.html', title='Upload Photo', form=form)


@bp.route('/photo/<id>')
@login_required
def view_photo(id):
    photo = Photo.objects(pk=id).first_or_404()
    user = User.objects(username=current_user.username).first_or_404()

    return render_template('photos/photo.html', title=f"{photo.title}", user=user, photo=photo)


@bp.route('/photos/like/<id>', methods=["GET", "POST"])
@login_required
def like_photo(id):
    photo = Photo.objects(pk=id).first_or_404()
    user = User.objects(username=current_user.username).first_or_404()

    if request.method =="POST":
        # Check for existing like by current user, remove if already liked, then update db
        if current_user in photo.liked_by_user:
            photo.update(dec__likes=1)
            photo.update(pull__liked_by_user=user.id)
            photo.save()
        # If user has not liked the photo, add a like and user liked by value, then update db
        else:
            photo.update(inc__likes=1)
            photo.update(push__liked_by_user=user.id)
            photo.save()
    
    return redirect(request.referrer)
