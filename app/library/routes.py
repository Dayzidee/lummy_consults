from flask import render_template, request
from app.library import bp
from app.models import LibraryItem
from app import db

@bp.route('/library')
def library_list():
    # Get filter parameters
    category = request.args.get('category', '')
    subject = request.args.get('subject', '')
    level = request.args.get('level', '')
    
    # Build query for approved items
    query = LibraryItem.query.filter(LibraryItem.status == 'approved')
    
    # Apply filters
    if category:
        query = query.filter(LibraryItem.category == category)
    if subject:
        query = query.filter(LibraryItem.subject.contains(subject))
    if level:
        query = query.filter(LibraryItem.level == level)
    
    library_items = query.order_by(LibraryItem.created_at.desc()).all()
    
    return render_template('library/list.html', library_items=library_items)

@bp.route('/library/item/<int:id>')
def library_detail(id):
    item = LibraryItem.query.get_or_404(id)
    return render_template('library/detail.html', item=item)

