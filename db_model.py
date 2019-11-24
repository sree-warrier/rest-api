import datetime
from app import db


class Post(db.Model):

    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False)

    def __init__(self, text, id):
        self.id = id
        self.text = text
        self.date_posted = datetime.datetime.now()


#create table posts (id int, text varchar(255), date_posted varchar(255))