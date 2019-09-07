from flask_mail import Message
from flask import render_template
from app import app
from app import mail
from threading import Thread

def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)

def send_email(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    Thread(target=send_async_email, args=(app, msg)).start()

def send_password_reset_email(user):
    token = user.get_reset_password_token()
    send_email('[Fondation] Reset Your Password',
               sender=app.config['ADMINS'][0],
               recipients=[user.email],
               text_body=render_template('email/reset_password.txt', user=user, token=token),
               html_body=render_template('email/reset_password.html', user=user, token=token))

def send_first_contact_email(email, name, message):
    send_email('[Fondation] New Message',
               sender=app.config.get("MAIL_USERNAME"),
               recipients=[app.config.get("MAIL_XAV"), app.config.get("MAIL_FLO")],
               text_body=render_template('email/contact_us.txt', email=email, name=name, message=message),
               html_body=render_template('email/contact_us.html', email=email, name=name, message=message))