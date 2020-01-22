from flask import Blueprint
from . import views

user = Blueprint('clients', __name__, url_prefix='/users', template_folder='templates')
