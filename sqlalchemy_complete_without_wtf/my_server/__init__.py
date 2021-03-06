from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from my_server.config import Config

app = Flask(__name__)

app.config.from_object(Config)

# Init db
db = SQLAlchemy(app)

from my_server import routes, models