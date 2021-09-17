import datetime
from flask import render_template, flash, redirect, url_for, request, abort
from flask_login import current_user, login_required
from cloudinary import uploader
from mongoengine.errors import NotUniqueError
from app.models import User, Photo, Comment
from app.photos import bp
from app.photos.forms import (UploadPhoto, AddComment,
                              EditPhotoForm, EditComment)


@bp.route('/feed')
@login_required
def photo_feed():
    # Gets page parameter, sets default page to 1,
    # type=int allows only ints to be passed
    page = request.args.get("page", 1, type=int)
    # Query db for all photo documents,
    # order by likes, pass in current page value
    photos = Photo.objects.order_by(
        '-likes', '-user_added_datetime').paginate(page=page, per_page=9)

    return render_template("photos/feed.html", photos=photos)


@bp.route('/upload', methods=["GET", "POST"])
@login_required
def upload_photo():
    # Create empty result variable to hold cloudinary file to upload
    upload_result = None
    form = UploadPhoto()
    # Check for post request and form validate on submit
    if request.method == "POST" and form.validate_on_submit():
        file_to_upload = request.files['file']

        if file_to_upload:
            try:
                # Set Cloudinary parameters for image upload
                upload_result = uploader.upload(
                    file_to_upload,
                    quality="auto",
                    fetch_format="auto",
                    allowed_formats=['png', 'jpg', 'jpeg'],
                    overwrite=True,
                    height=1920,
                    width=1080,
                    crop="fit",
                    moderation="aws_rek"
                )
                # Populate Photo object with form inputs and save to mongoDB
                new_photo = Photo(
                    title=form.title.data,
                    description=form.description.data,
                    user_uploaded_by=current_user.username,
                    user_added_datetime=datetime.datetime.utcnow,
                    url=upload_result["secure_url"],
                    public_id=upload_result["public_id"])
                new_photo.save()
                flash("New photo added!")
                return redirect(url_for('main.profile',
                                        username=current_user.username))
            except NotUniqueError:
                # If user manages to submit an upload request multiple times,
                # this logic returns them to their profile once cloudinary
                # upload is complete, but supresses mongoengine
                # duplicate key error.
                return redirect(url_for('main.profile',
                                        username=current_user.username))

    return render_template('photos/upload.html',
                           title='Upload Photo', form=form)


@bp.route('/edit/<id>', methods=["GET", "POST"])
@login_required
def edit_photo(id):
    photo = Photo.objects(pk=id).first_or_404()

    form = EditPhotoForm(title=photo.title, description=photo.description)

    if photo.user_uploaded_by != current_user.username:
        flash('You can only edit your own photos!')
        return redirect(url_for('main.index'))
    if request.method == "POST":
        photo.update(title=form.title.data)
        photo.update(description=form.description.data)
        photo.save()
        flash("Your photo has been updated!")
        return redirect(url_for('photos.view_photo', id=photo.id))
    elif request.method == "GET":
        form.title.data = photo.title
        form.description.data = photo.description

    return redirect(url_for('photos.view_photo', id=photo.id))


@bp.route('/<id>')
@login_required
def view_photo(id):
    photo = Photo.objects(pk=id).first_or_404()
    user = User.objects(username=current_user.username).first_or_404()
    comments = Comment.objects(
        photo_commented_on=id).order_by(
        '-user_comment_datetime')
    commentform = AddComment()
    editphotoform = EditPhotoForm()
    editcommentform = EditComment()

    return render_template('photos/photo.html', title=f"{photo.title}",
                           user=user, photo=photo, commentform=commentform,
                           editphotoform=editphotoform,
                           editcommentform=editcommentform,
                           comments=comments)


@bp.route('/like/<id>', methods=["GET", "POST"])
@login_required
def like_photo(id):
    photo = Photo.objects(pk=id).first_or_404()
    user = User.objects(username=current_user.username).first_or_404()

    if request.method == "POST":
        # Check for existing like by current user,
        # remove if already liked, then update db
        if current_user in photo.liked_by_user:
            photo.update(dec__likes=1)
            photo.update(pull__liked_by_user=user.id)
            photo.save()
        # If user has not liked the photo, add a like and user's ID,
        # then update db
        else:
            photo.update(inc__likes=1)
            photo.update(push__liked_by_user=user.id)
            photo.save()

    return redirect(request.referrer)


@bp.route('/comment/<id>', methods=["GET", "POST"])
@login_required
def add_comment(id):
    user = User.objects(username=current_user.username).first_or_404()
    photo = Photo.objects(pk=id).first_or_404()

    form = AddComment()
    if request.method == "POST" and form.validate_on_submit():
        # Add new comment to DB
        new_comment = Comment(
            user_comment_by=user,
            user_comment_datetime=datetime.datetime.utcnow,
            photo_commented_on=photo,
            comment_text=form.comment_text.data,
            likes=0
        )
        new_comment.save()
        flash("Thanks for the comment!")

    return redirect(url_for('photos.view_photo', id=photo.id))


@bp.route('/like_comment/<id>', methods=["GET", "POST"])
@login_required
def like_comment(id):
    comment = Comment.objects(pk=id).first_or_404()
    user = User.objects(username=current_user.username).first_or_404()

    if request.method == "POST":
        # Check for existing like by current user,
        # remove if already liked, then update db
        if current_user in comment.liked_by_user:
            comment.update(dec__likes=1)
            comment.update(pull__liked_by_user=user.id)
            comment.save()
        # If user has not liked the comment,
        # add a like and user liked by value,
        # then update db
        else:
            comment.update(inc__likes=1)
            comment.update(push__liked_by_user=user.id)
            comment.save()

    return redirect(request.referrer)


@bp.route('/edit_comment/<id>', methods=["GET", "POST"])
@login_required
def edit_comment(id):
    comment = Comment.objects(pk=id).first_or_404()

    # Confirm current user is the comment creator
    if current_user.id != comment.user_comment_by.id:
        flash('You can only edit your own comments!')
        abort(403)

    form = EditComment()
    if request.method == "POST":
        # Edit comment and save changes to DB
        comment.update(comment_text=form.comment_text.data)
        comment.update(user_comment_datetime=datetime.datetime.utcnow)
        comment.save()
        flash('Your comment has been updated!')
        return redirect(request.referrer)
    elif request.method == "GET":
        form.comment_text.data = comment.comment_text

    return redirect(request.referrer)


@bp.route('/delete_comment/<id>', methods=["POST"])
@login_required
def delete_comment(id):
    comment = Comment.objects(pk=id).first_or_404()
    photo = comment.photo_commented_on

    # Confirm current user is the comment creator
    if current_user.id != comment.user_comment_by.id:
        flash('You can only delete your own comments!')
        abort(403)
    if request.method == "POST":
        comment.delete()
        flash('Your comment has been deleted.')
        return redirect(url_for('photos.view_photo', id=photo.id))


@bp.route('/delete_photo/<id>', methods=["POST"])
@login_required
def delete_photo(id):
    photo = Photo.objects(pk=id).first_or_404()
    user = User.objects(username=current_user.username).first_or_404()
    # Confirm current user is the comment creator
    if user.username != photo.user_uploaded_by:
        flash('You can only delete your own photos!')
        abort(403)
    if request.method == "POST":
        photo.delete_photo_db()
        photo.delete()
        flash('Your photo has been deleted.')
        return redirect(url_for('main.profile',
                                username=current_user.username))
