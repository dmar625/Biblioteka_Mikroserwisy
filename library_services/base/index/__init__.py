from flask import Blueprint

main = Blueprint('base', __name__, template_folder='templates')
from . import views
