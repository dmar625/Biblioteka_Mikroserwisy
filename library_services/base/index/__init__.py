from flask import Blueprint
from . import views

main = Blueprint('base', __name__, template_folder='templates')
