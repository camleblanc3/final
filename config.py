import os

#set up base directory of entire application
basedir = os.path.abspath(os.path.dirname(__name__))

#CONFIG variables set up
class Config:
    """
    set configuration variables for entire flask app
    """
    FLASK_APP = os.environ.get('FLASK_APP')
    FLASK_ENV = os.environ.get('FLASK_ENV')
    SECRET_KEY = os.environ.get('SECRET_KEY')