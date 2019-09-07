from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import ContactForm
from app.forms import SignInForm
from flask_login import current_user, login_user
from app.models import User
from flask_login import logout_user
from flask_login import login_required
from flask import request
from werkzeug.urls import url_parse
from app import db
from app.forms import SignUpForm
from app.email import send_first_contact_email
from datetime import datetime
from app.forms import EditProfileForm
from app.forms import ResetPasswordRequestForm
from app.email import send_password_reset_email
from app.forms import ResetPasswordForm

@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()

@app.route("/home")
@app.route("/")
def home():
    return render_template("home.html")

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if current_user.is_authenticated:
        flash('already authenticated under login: ' + current_user.email )
        return redirect(url_for('home'))
    form = SignInForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('signin'))
        login_user(user, remember=form.remember_me.data)
        flash('Welcome '+user.first_name + ' ' + user.last_name)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('home')
        return redirect(next_page)
    return render_template('signin.html', title='Sign in', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/user_profile/<email>')
@login_required
def user_profile(email):
    if not current_user.is_authenticated:
        return redirect(url_for('signin'))
    user = User.query.filter_by(email=email).first_or_404()
    posts = [
        {'author': user, 'body': 'rejected'},
        {'author': user, 'body': 'received'}
    ]
    return render_template('user_profile.html', user=user, posts=posts)

@app.route('/edit_user_profile', methods=['GET', 'POST'])
@login_required
def edit_user_profile():
    if not current_user.is_authenticated:
        return redirect(url_for('signin'))
    form = EditProfileForm()
    if form.validate_on_submit():
        current_user.first_name = form.first_name.data
        current_user.last_name = form.last_name.data
        current_user.about_me = form.about_me.data
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('edit_user_profile'))
    elif request.method == 'GET':
        form.first_name.data = current_user.first_name
        form.last_name.data = current_user.last_name
        form.about_me.data = current_user.about_me
    return render_template('edit_user_profile.html', title='Edit Profile',
                           form=form)


@app.route('/pre_approval')
def pre_approval():
    if not current_user.is_authenticated:
        return redirect(url_for('signin'))
    return render_template("pre_approval.html")

@app.route('/pre_application')
@login_required
def pre_application():
    return render_template("pre_application.html")

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template("dashboard.html")

@app.route("/contact_us", methods=['GET', 'POST'])
def contact_us():
    form = ContactForm()
    if form.validate_on_submit():
        send_first_contact_email(form.email.data, form.full_name.data, form.message.data)
        flash('Your has been sent. We will get back to you shortly')
        return redirect(url_for('contact_us'))
    return render_template("contact_us.html", title='Contact', form=form)
@app.route("/faq")
def faq():
    return render_template("faq.html")

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        flash('already authenticated under login: ' + current_user.email )
        return redirect(url_for('home'))
    form = SignUpForm()
    if form.validate_on_submit():
        user = User(first_name=form.first_name.data,last_name=form.last_name.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('signin'))
    return render_template('signup.html', title='Sign up', form=form)


@app.route('/reset_password_request', methods=['GET', 'POST'])
def reset_password_request():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = ResetPasswordRequestForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            send_password_reset_email(user)
        flash('Check your email for the instructions to reset your password')
        return redirect(url_for('signin'))
    return render_template('reset_password_request.html',
                           title='Reset Password', form=form)

@app.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    user = User.verify_reset_password_token(token)
    if not user:
        return redirect(url_for('home'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        user.set_password(form.password.data)
        db.session.commit()
        flash('Your password has been reset.')
        return redirect(url_for('signin'))
    return render_template('reset_password.html', form=form)

@app.errorhandler(404)
def not_found_error(error):
    return render_template('error.html')

@app.errorhandler(500)
def internal_error(error):
    return render_template('error.html')