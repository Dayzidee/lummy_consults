from flask import render_template
from app.admin import bp

@bp.route('/dashboard')
def admin_dashboard():
    # Placeholder for admin dashboard logic
    return render_template('admin/dashboard.html')

