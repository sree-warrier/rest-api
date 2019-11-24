__author__ = 'sree-warrier'

from flask import Flask
from flask import request, render_template
from flask_sqlalchemy import SQLAlchemy
from db_config import DbConfig


# Create the application instance
app = Flask(__name__, template_folder="templates")
app.config.from_object(DbConfig)
db = SQLAlchemy(app)


from db_model import *

# Create a URL route in our application for "/"
@app.route('/api/message', methods=['POST'])
def newMessage():
    #if request.method == 'POST':
    message = request.form['text']
    post = Post(message)
    #print(Post)
    db.session.add(post)
    db.session.commit()
    posts = Post.query.order_by(Post.date_posted.desc()).all()
    return render_template('home.html', posts=posts)

# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(
        debug=True,
        host="0.0.0.0",
        port="8080"
    )