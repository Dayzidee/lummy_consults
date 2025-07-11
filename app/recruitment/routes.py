from flask import render_template, request
from app.recruitment import bp
from app.models import JobPosting
from app import db

@bp.route('/jobs')
def job_list():
    # Get filter parameters
    keyword = request.args.get('keyword', '')
    location = request.args.get('location', '')
    job_type = request.args.get('job_type', '')
    
    # Build query
    query = JobPosting.query.filter(JobPosting.status == 'active')
    
    # Apply filters
    if keyword:
        query = query.filter(
            db.or_(
                JobPosting.title.contains(keyword),
                JobPosting.company_name.contains(keyword),
                JobPosting.description.contains(keyword)
            )
        )
    if location:
        query = query.filter(JobPosting.location.contains(location))
    if job_type:
        query = query.filter(JobPosting.job_type == job_type)
    
    jobs = query.order_by(JobPosting.created_at.desc()).all()
    
    return render_template('recruitment/list.html', jobs=jobs)

@bp.route('/job/<int:id>')
def job_detail(id):
    job = JobPosting.query.get_or_404(id)
    return render_template('recruitment/detail.html', job=job)

