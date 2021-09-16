from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_required
from app.main.forms import EditProfileForm
from app.models import User, Photo
from app.main import bp


@bp.route('/')
@bp.route('/index')
def index():
    if current_user.is_authenticated == False:
        flash("Welcome, please log in or register to access the site!")
        return render_template('index.html')
    else:
        return redirect(url_for('photos.photo_feed'))
 

@bp.route('/profile/<username>')
@login_required
def profile(username):
    page = request.args.get("page", 1, type=int)
    user = User.objects(username=username).first_or_404()
    photos = Photo.objects(user_uploaded_by=user.username).paginate(page=page, per_page=9)

    return render_template('profile.html', title=f"{user.username}'s Profile", user=user, photos=photos)


@bp.route('/edit_profile/<id>', methods=["GET", "POST"])
@login_required
def edit_profile(id):
    user = User.objects.get_or_404(pk=id)
    # Check for match of user's username against session username
    if user != current_user:
        flash('You can only edit your own profile!')
        return redirect(url_for('main.profile'))
    form = EditProfileForm()
    # Update form logic on post request
    if form.validate_on_submit():
        color = user.avatar
        avatar_num = user.avatar_num
        if form.avatar.data == "1":
            color = "#E60023"
            avatar_num = "1"
        elif form.avatar.data == "2":
            color = "#E6C300"
            avatar_num = "2"
        elif form.avatar.data == "3":
            color = "#00E6C3"
            avatar_num = "3"
        elif form.avatar.data == "4":
            color = "#0022E6"
            avatar_num = "4"
        else:
            pass
        user.about_me = form.about_me.data
        user.avatar = color
        user.avatar_num = avatar_num
        user.save()
        flash("Your account has been updated!")
        return redirect(url_for('main.profile', username=user.username))
    # Populate form with existing data on get request
    elif request.method == "GET":
        form.about_me.default = user.about_me
        form.avatar.default = user.avatar_num
        form.process()

    return render_template('edit_profile.html', title='Edit Profile', 
        legend='Edit Profile', user=user, form=form)
