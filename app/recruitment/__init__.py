from flask import Blueprint

bp = Blueprint('recruitment', __name__)

from app.recruitment import routes

