from flask import Flask
from my_server.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config)

# Init db
db = SQLAlchemy(app)

# Init Login Manager
login_manager = LoginManager(app)
# Here the function name for the login route is passed in.
# This is needed in order for @login_required to function.
# It then sends the user to this page when they try to access
# a page they are not entitled to enter.

# message_category makes the flash message nicer

#The "next query" in the GET request can be used to send the user
# to the right landing page once they have logged in. This can
# be done in the "/login" route
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from my_server import routes