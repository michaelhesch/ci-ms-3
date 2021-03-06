from flask import render_template, flash, redirect, url_for, request, session
from flask_login import current_user, login_user, logout_user
from werkzeug.urls import url_parse
from mongoengine.errors import NotUniqueError, DoesNotExist
from app.auth.forms import LoginForm, RegistrationForm
from app.models import User
from app.auth import bp


@bp.route('/login', methods=["GET", "POST"])
def login():
    # Redirect user to index if already logged in
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    # Login form handling if not logged in
    form = LoginForm()

    # Catch mongoengine error for username not found in DB
    if request.method == "POST" and form.validate_on_submit():
        try:
            user = User.objects.get(username=form.username.data.lower())
            # Check for incorrect credentials
            if user is None or not user.check_password(form.password.data):
                flash('Incorrect login details, please try again.')
                return redirect(url_for('auth.login'))
            login_user(user, remember=form.remember_me.data)
            # Set session to permanent to enable automatic timeout
            session.permanent = True
            # Check for next argument from login_required action
            next_page = request.args.get('next')
            # If next argument not passed, redirect to index
            if not next_page or url_parse(next_page).netloc != '':
                next_page = url_for('main.index')
            # Else if next is found, redirects to user's desired page
            # once logged in
            return redirect(next_page)

        except DoesNotExist:
            flash('Incorrect login details, please try again.')
            return redirect(request.referrer)

    return render_template('auth/login.html', title='Sign In', form=form)


@bp.route('/register', methods=["GET", "POST"])
def register():
    # Send user to homepage if already registered & logged in
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = RegistrationForm()
    if request.method == "POST" and form.validate_on_submit():
        try:
            color = None
            if form.avatar.data == "1":
                color = "#E60023"
            elif form.avatar.data == "2":
                color = "#E6C300"
            elif form.avatar.data == "3":
                color = "#00E6C3"
            elif form.avatar.data == "4":
                color = "#0022E6"
            else:
                pass

            user = User(
                username=form.username.data.lower(),
                email=form.email.data,
                first_name=form.first_name.data.lower(),
                last_name=form.last_name.data.lower(),
                avatar=color,
                avatar_num=form.avatar.data)
            user.set_password(form.password.data)
            user.save()
            login_user(user)
            flash("You have registered a new account!")
            return redirect(url_for('main.index'))

        except NotUniqueError:
            """
            Handles Mongoengine duplicate key value error
            returned when a user provides a username or email
            that already exists in the db.
            """
            flash("The username or email already exists, please try again.")
            return redirect(request.referrer)

    return render_template('auth/register.html', title='Register', form=form)


@bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))
