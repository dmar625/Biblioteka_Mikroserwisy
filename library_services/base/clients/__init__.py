from flask import Blueprint

user = Blueprint('clients', __name__, url_prefix='/users', template_folder='templates')
from . import views
