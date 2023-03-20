from flask import Blueprint


bp = Blueprint('v1', __name__)

from app.api.v1 import routes
