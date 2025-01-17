from distutils.command.config import config
import os
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database

SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:abolarin@localhost:5432/fyyurdb'


SQLALCHEMY_TRACK_MODIFICATIONS = True

WTF_CSRF_ENABLED = False
