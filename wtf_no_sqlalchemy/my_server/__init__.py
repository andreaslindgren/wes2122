from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from my_server.config import Config
import os

app = Flask(__name__)
app.config.from_object(Config)

#Database
#basedir = os.path.abspath(os.path.dirname((__file__)))
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')

# Init db
db = SQLAlchemy(app)

from my_server import routes, models