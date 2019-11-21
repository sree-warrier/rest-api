__author__ = 'sree-warrier'
import os

class DbConfig(object):
    #SECRET_KEY = os.environ['SECRET_KEY']
    #DEBUG = os.environ['DEBUG']
    DB_NAME = os.environ['SQLAlchemy']
    DB_USER = os.environ['admin']
    DB_PASS = os.environ['Admin12345']
    DB_SERVICE = os.environ['messanger-db.cq5piu3seb1e.ap-southeast-1.rds.amazonaws.com']
    DB_PORT = os.environ['3306']
    SQLALCHEMY_DATABASE_URI = 'mysql://{0}:{1}@{2}/{3}'.format(
        DB_USER, DB_PASS, DB_SERVICE, DB_NAME
    )


#class DbConfig(object):
    #SECRET_KEY = os.environ['SECRET_KEY']
    #DEBUG = os.environ['DEBUG']
    #DB_NAME = os.environ['DB_NAME']
    #DB_USER = os.environ['DB_USER']
    #DB_PASS = os.environ['DB_PASS']
    #DB_SERVICE = os.environ['DB_SERVICE']
    #DB_PORT = os.environ['DB_PORT']
    #SQLALCHEMY_DATABASE_URI = 'mysql://{0}:{1}@{2}/{3}'.format(
    #    DB_USER, DB_PASS, DB_SERVICE, DB_NAME
    #)