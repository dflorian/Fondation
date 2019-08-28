from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)

mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": 'snoopy.bollart@gmail.com',
    "MAIL_PASSWORD": 'YJZ-4DA-zDd-T8H'
}

app.config.update(mail_settings)
mail = Mail(app)

if __name__ == '__main__':
    with app.app_context():
        msg = Message(subject="Hello",
                      sender=app.config.get("MAIL_USERNAME"),
                      recipients=["xavier.bollart@gmail.com"], # replace with your email for testing
                      body="This is a test email I sent with Gmail and Python!")
        mail.send(msg)