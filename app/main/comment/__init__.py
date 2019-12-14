from flask import Blueprint
from . import views

comment = Blueprint('comment', __name__, url_prefix='/comments')

