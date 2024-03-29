__author__ = 'sree-warrier'
import os


class DbConfig(object):
    #SECRET_KEY = os.environ['SECRET_KEY']
    #DEBUG = os.environ['DEBUG']
    DB_NAME = os.environ['DB_NAME']
    DB_USER = os.environ['DB_USER']
    DB_PASS = os.environ['DB_PASS']
    DB_SERVICE = os.environ['DB_SERVICE']
    DB_PORT = os.environ['DB_PORT']
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{0}:{1}@{2}/{3}'.format(
        DB_USER, DB_PASS, DB_SERVICE, DB_NAME
    )