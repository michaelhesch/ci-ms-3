from app import app
from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse
from app.forms import EditProfileForm, LoginForm, RegistrationForm
from app.models import User

@app.route('/')
@app.route('/index')
@login_required
def index():
    posts = [
        {
        'author': {'username': 'John'},
        'body': 'Beautiful day in Portland!'
        },
        {
        'author': {'username': 'Susan'},
        'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', posts=posts)


@app.route('/login', methods=["GET", "POST"])
def login():
    # Redirect user to index if already logged in
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    # Login form handling if not logged in
    form = LoginForm()
    if form.validate_on_submit():
        user = User.objects.get(username=form.username.data.lower())
        if user is None or not user.check_password(form.password.data):
            flash('Incorrect login details, please try again.')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        # Check for next argument from login_required action
        next_page = request.args.get('next')
        # If next argument not passed, redirect to index
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        # Else if next is found, redirects to user's desired page 
        # once logged in
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)


@app.route('/register', methods=["GET", "POST"])
def register():
    # Send user to homepage if already registered & logged in
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(
            username=form.username.data.lower(),
            email=form.email.data,
            first_name=form.first_name.data.lower(),
            last_name=form.last_name.data.lower())
        user.set_password(form.password.data)
        user.save()
        login_user(user)
        flash("You have registered a new account!")
        return redirect(url_for('index'))
    return render_template('register.html', title='Register', form=form)


@app.route('/profile/<username>')
@login_required
def profile(username):
    # Checks for username match, returns 404 error if no match found
    user = User.objects(username=username).first_or_404()
    return render_template('/profile.html', title=f"{user.username}", user=user)


@app.route('/edit_profile/<id>', methods=["GET", "POST"])
@login_required
def edit_profile(id):
    user = User.objects.get(pk=id)
    # Check for match of user's username against session username
    if user != current_user:
        flash('You can only edit your own profile!')
        return redirect(url_for('index'))
    form = EditProfileForm()
    # Update form logic on post request
    if form.validate_on_submit():
        user.about_me = form.about_me.data
        user.save()
        flash("Your account has been updated!")
        return redirect(url_for('profile', username=user.username))
    # Populate form with existing data on get request
    elif request.method == "GET":
        form.about_me.data = user.about_me
    return render_template('edit_profile.html', title='Edit Profile', user=user, form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
