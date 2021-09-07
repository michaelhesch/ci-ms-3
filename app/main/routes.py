from app import db
from flask import render_template, flash, redirect, url_for, request, current_app
from flask_login import current_user, login_required
from app.main.forms import EditProfileForm
from app.models import User, Photo
from app.main import bp

@bp.route('/')
@bp.route('/index')
def index():
    if current_user.is_authenticated == False:
        return redirect(url_for('auth.login'))

    return render_template('index.html', title='Home')


@bp.route('/profile/<username>')
@login_required
def profile(username):
    # Checks for username match, returns 404 error if no match found
    user = User.objects(username=username).first_or_404()
    photos = list(Photo.objects)
    return render_template('profile.html', title=f"{user.username}", user=user, photos=photos)


@bp.route('/edit_profile/<id>', methods=["GET", "POST"])
@login_required
def edit_profile(id):
    user = User.objects.get_or_404(pk=id)
    # Check for match of user's username against session username
    if user != current_user:
        flash('You can only edit your own profile!')
        return redirect(url_for('main.index'))
    form = EditProfileForm()
    # Update form logic on post request
    if form.validate_on_submit():
        user.about_me = form.about_me.data
        user.save()
        flash("Your account has been updated!")
        return redirect(url_for('main.profile', username=user.username))
    # Populate form with existing data on get request
    elif request.method == "GET":
        form.about_me.data = user.about_me
    return render_template('edit_profile.html', title='Edit Profile', user=user, form=form)
