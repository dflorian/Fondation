import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = 'you-will-never-guess'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = 'snoopy.bollart@gmail.com'
    MAIL_PASSWORD = 'YJZ-4DA-zDd-T8H'
    MAIL_XAV = 'xavier.bollart@gmail.com'
    MAIL_FLO = 'fdoumenc@gmail.com'
    APP_IP = '127.0.0.1'
    APP_PORT = 8080
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ADMINS = ['xavier.bollart@gmail.com']




class ProductionConfig(Config):
    APP_IS_DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://admin:admin@/fondation_db?unix_socket=/cloudsql/fondation:us-east1:fondation-db'

class ProductionRemoteConfig(Config):
    APP_IS_DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://admin:admin@127.0.0.1:3307/fondation_db'

class DevelopmentConfig(Config):
    APP_IS_DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:Geekms01@localhost/fondation_db'
  #  SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')

class TestingConfig(Config):
    APP_IS_DEBUG = False