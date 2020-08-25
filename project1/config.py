import os

class Config(object):
    SECRET_KEY = "mi_palabra_secreta"

class DevelopmentConfig(Config):
    DEBUG= True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:@localhost/flaks'
