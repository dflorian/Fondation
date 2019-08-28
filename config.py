import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess',
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = 465,
    MAIL_USE_TLS = False,
    MAIL_USE_SSL = True,
    MAIL_USERNAME = 'snoopy.bollart@gmail.com',
    MAIL_PASSWORD = 'YJZ-4DA-zDd-T8H',
    MAIL_RECIPIENT = 'xavier.bollart@gmail.com'
