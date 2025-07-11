from flask import Blueprint

bp = Blueprint('tutors', __name__)

from app.tutors import routes

