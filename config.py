import os

basedir = os.path.abspath(os.path.dirname(__file__))
DATABASE = os.path.join(basedir, 'app.db')

MAX_CONTENT_LENGTH = 1024 * 1024

UPLOADS_DEFAULT_DEST = os.path.join(basedir, 'upload/')

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE

SECRET_KEY = '1234'

FLASK_ADMIN = 'darek@gmail.com'

SQLALCHEMY_TRACK_MODIFICATIONS = False