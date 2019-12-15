import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_pagedown import PageDown
from flask_uploads import UploadSet, IMAGES, configure_uploads
from app.main import main, auth, user, book, comment, log
from app.api import api_bp
from app import models

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
lm = LoginManager(app)
bootstrap = Bootstrap(app)
pagedown = PageDown(app)
avatars = UploadSet('avatars', IMAGES)
configure_uploads(app, avatars)


for blueprint in [main, auth, user, book, comment, log, api_bp]:
    app.register_blueprint(blueprint)


exists_db = os.path.isfile(app.config['DATABASE'])
if not exists_db:
    from . import database
