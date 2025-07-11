from flask import Blueprint
import json

bp = Blueprint('tutors', __name__)

# Define the template filter at the blueprint level
@bp.app_template_filter('from_json')
def from_json_filter(value):
    try:
        return json.loads(value) if value else []
    except (json.JSONDecodeError, TypeError): # Be more specific with exception handling
        return []

from app.tutors import routes

