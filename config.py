

class Config(object):
    SECRET_KEY = 'you-will-never-guess'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = 'snoopy.bollart@gmail.com'
    MAIL_PASSWORD = 'YJZ-4DA-zDd-T8H'
    MAIL_XAV = 'xavier.bollart@gmail.com'
    MAIL_FLO = ''
    IP = '127.0.0.1'
    PORT = 8080
    IS_DEBUG = True


class ProductionConfig(Config):
    DATABASE_URI = 'mysql://user@localhost/foo'

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True