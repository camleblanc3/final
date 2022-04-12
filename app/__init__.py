from flask import Flask
import pyrebase
from config import Config

from .auth.auth import auth

app = Flask(__name__)
app.config.from_object(Config)

app.register_blueprint(auth)

from . import routes 