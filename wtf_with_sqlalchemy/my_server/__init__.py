from flask import Flask
from my_server.config import Config
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(Config)

# Init db
db = SQLAlchemy(app)

from my_server import routes