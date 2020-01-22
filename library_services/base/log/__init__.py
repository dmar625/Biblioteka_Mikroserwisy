from flask import Blueprint
from . import views

log = Blueprint('log', __name__, url_prefix='/logs_info', template_folder='templates')
