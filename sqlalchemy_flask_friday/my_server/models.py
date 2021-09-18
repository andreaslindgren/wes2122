from my_server import db
from datetime import datetime

# User Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    date_added = db.Column(db.DateTime, default=datetime.utcnow())

    def __init__(self, name, email):
        self.name = name
        self.email = email
    
    def __repr__(self):
        return '<Name %r>' % self.name


