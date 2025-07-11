from flask import render_template, request
from app.tutors import bp
from app.models import TutorProfile, User
from app import db
import json

@bp.route('/tutors')
def tutor_list():
    # Get filter parameters
    subject = request.args.get('subject', '')
    level = request.args.get('level', '')
    location = request.args.get('location', '')
    
    # Build query
    query = TutorProfile.query.join(User).filter(User.is_approved == True)
    
    # Apply filters
    if subject:
        query = query.filter(TutorProfile.subjects.contains(subject))
    if level:
        query = query.filter(TutorProfile.teaching_levels.contains(level))
    if location:
        query = query.filter(TutorProfile.location.contains(location))
    
    tutors = query.all()
    
    # Add JSON parsing filter to Jinja
    @bp.app_template_filter('from_json')
    def from_json_filter(value):
        try:
            return json.loads(value) if value else []
        except:
            return []
    
    return render_template('tutors/list.html', tutors=tutors)

@bp.route('/tutor/<int:id>')
def tutor_detail(id):
    tutor = TutorProfile.query.get_or_404(id)
    return render_template('tutors/detail.html', tutor=tutor)

