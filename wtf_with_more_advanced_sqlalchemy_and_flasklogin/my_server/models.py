from my_server import db, login_manager
from datetime import datetime
from flask_login import UserMixin

# Needed in order for login_manager to work
# Needs to get an instance of class User, given a user id
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# User Model
# Added "UserMixin" class, in order to add functionality for 
# "is_authenticated", "is_active", "is_anonymous" and "get_id". All of these
# are included in the UserMixin
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    date_added = db.Column(db.DateTime, default=datetime.utcnow())
    
    #reference to another table. Lazy=true means SQLAlchemy loads all necessary data in one go.
    #not a column – it's a relationship. Does not show in the database. It's just an additional query
    #Upper-case P because we're referencing the Post class
    posts = db.relationship('Post', backref='author', lazy=True)
    
    # Similar to "toString" in Java. What happens when an instance of theh class is printed.
    # To test: print(User.query.all()) eller print(User.query.first())
    def __repr__(self):
        return f'Username: {self.username}'

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    #Lower case u in user, because we're referencing the user table (not the class)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    date_added = db.Column(db.DateTime, default=datetime.utcnow())

    # Similar to "toString" in Java. What happens when an instance of theh class is printed.
    def __repr__(self):
        return f'Post content: {self.content}'

    # To create database: in python:
    # from my_server import db
    # db.create_all()