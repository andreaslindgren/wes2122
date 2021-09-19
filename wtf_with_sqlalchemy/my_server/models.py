from my_server import db
from datetime import datetime

# User Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    date_added = db.Column(db.DateTime, default=datetime.utcnow())
    
    # Similar to "toString" in Java. What happens when an instance of theh class is printed.
    # To test: print(User.query.all()) eller print(User.query.first())
    def __repr__(self):
        return f'Username: {self.username}'

# To create database: in python:
# from my_server import db
# db.create_all()