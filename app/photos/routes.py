from app import db
from flask import render_template, flash, redirect, url_for, request, current_app
from flask_login import current_user, login_required
# from app.photos.forms import 
from app.models import User, Photo
from app.photos import bp
from app.photos.forms import UploadPhoto
import datetime
from cloudinary import uploader


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
