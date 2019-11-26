__author__ = 'sree-warrier'

from flask import Flask
from flask import request, render_template
from flask_sqlalchemy import SQLAlchemy
from db_config import DbConfig
import time

# Create the application instance
app = Flask(__name__, template_folder="templates")
app.config.from_object(DbConfig)
db = SQLAlchemy(app)


from db_model import *

@app.route('/')
def homePage():
    return render_template('home.html')

# Create a URL route in our application for "/"
@app.route('/api/message', methods=['POST'])
def addMsg():
    text = request.form['text']
    post = Post(text)
    db.session.add(post)
    db.session.commit()
    posts = Post.query.order_by(Post.date_posted.desc()).all()
    return render_template('output.html', posts=posts)

@app.route('/api/message', methods=['GET'])
def listMsg():
    listall = Post.query.order_by(Post.text).all()
    return render_template('output3.html', listall=listall)

@app.route('/api/message/<msg_id>', methods=['GET'])
def getMsgId(msg_id):
    message = Post.query.get(msg_id).text
    return render_template('output1.html', message=message)

@app.route('/api/message/<msg_id>', methods=['DELETE'])
def delMsg(msg_id):
    delmessage = Post.query.filter_by(id=msg_id).first()
    db.session.delete(delmessage)
    db.session.commit()
    return render_template('output2.html')

# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(
        debug=True,
        host="0.0.0.0",
        port="8080"
    )