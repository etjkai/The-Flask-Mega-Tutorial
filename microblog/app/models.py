from app import db, login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship("Post", backref="author", lazy="dynamic")
    # Adds 'posts' attribute to users - u.posts = <sqlalchemy.orm.dynamic.AppenderBaseQuery object at 0x03B844A8>
    ## Returns all the posts written by that user.
    # Adds 'author' attribute to posts - p.author = <User John>
    # backref argument defines the name of a field added to the objects of the "many" Class, that then points back at the "one" object.

    def set_password(self, password):
        # Sets the instance attribute
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f"<User {self.username}>"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    # Adds 'author' attribute to posts - p.author = <User John>

    def __repr__(self):
        return f"<Post {self.body}>"


# Load a user given the ID
@login.user_loader
def load_user(id):
    return User.query.get(int(id))
