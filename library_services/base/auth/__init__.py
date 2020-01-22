from flask import Blueprint
from . import views

auth = Blueprint('auth', __name__, template_folder='templates')

