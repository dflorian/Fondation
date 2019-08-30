from app import app
from flask import render_template, flash, redirect, url_for
from app.contact_form import ContactForm
from flask_mail import Message
# from app.forms import ResetPasswordRequestForm
from app.email import send_first_contact_email
# from app.forms import ResetPasswordForm
from app import mail

@app.route("/home/")
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about/")
def about():
    return render_template("about.html")

@app.route("/contact/", methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        send_first_contact_email(form.email.data, form.full_name.data)
        flash('Your email has been added to our client database'.format(
            form.full_name.data, form.email.data))
        return redirect(url_for('contact'))
    return render_template("contact.html", title='Contact', form=form)

@app.route("/faq/")
def faq():
    return render_template("faq.html")

# @app.route('/reset_password_request', methods=['GET', 'POST'])
# def reset_password_request():
#     if current_user.is_authenticated:
#         return redirect(url_for('index'))
#     form = ResetPasswordRequestForm()
#     if form.validate_on_submit():
#         user = User.query.filter_by(email=form.email.data).first()
#         if user:
#             send_password_reset_email(user)
#         flash('Check your email for the instructions to reset your password')
#         return redirect(url_for('login'))
#     return render_template('reset_password_request.html',
#                            title='Reset Password', form=form)
#
# @app.route('/reset_password/<token>', methods=['GET', 'POST'])
# def reset_password(token):
#     if current_user.is_authenticated:
#         return redirect(url_for('index'))
#     user = User.verify_reset_password_token(token)
#     if not user:
#         return redirect(url_for('index'))
#     form = ResetPasswordForm()
#     if form.validate_on_submit():
#         user.set_password(form.password.data)
#         db.session.commit()
#         flash('Your password has been reset.')
#         return redirect(url_for('login'))
#     return render_template('reset_password.html', form=form)

@app.errorhandler(404)
def not_found_error(error):
    return render_template('error.html')

@app.errorhandler(500)
def internal_error(error):
    return render_template('error.html')