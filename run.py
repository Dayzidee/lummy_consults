#!/usr/bin/env python3
"""
Lummy Consults - Main Application Runner

This is the main entry point for the Lummy Consults application.
It creates the Flask app instance and runs the development server.

Usage:
    python run.py

Environment Variables:
    FLASK_CONFIG: Configuration mode (development, production, testing)
    FLASK_ENV: Flask environment (development, production)
    FLASK_DEBUG: Enable debug mode (True, False)
"""

import os
from app import create_app, db
from app.models import User, TutorProfile, StudentProfile, JobPosting, LibraryItem
from flask_migrate import Migrate

# Get configuration from environment or use default
config_name = os.getenv('FLASK_CONFIG', 'development')
from config import config
app = create_app(config[config_name])
migrate = Migrate(app, db)

# Shell context for Flask CLI
@app.shell_context_processor
def make_shell_context():
    """Make database models available in Flask shell"""
    return {
        'db': db,
        'User': User,
        'TutorProfile': TutorProfile,
        'StudentProfile': StudentProfile,
        'JobPosting': JobPosting,
        'LibraryItem': LibraryItem
    }

# CLI command to create sample data
@app.cli.command()
def create_sample_data():
    """Create sample data for testing"""
    from datetime import datetime
    import json
    
    # Create sample users
    users_data = [
        {
            'username': 'admin',
            'email': 'admin@lummyconsults.com',
            'first_name': 'Admin',
            'last_name': 'User',
            'role': 'admin',
            'password': 'admin123'
        },
        {
            'username': 'john_tutor',
            'email': 'john@lummyconsults.com',
            'first_name': 'John',
            'last_name': 'Adebayo',
            'role': 'tutor',
            'password': 'password123'
        },
        {
            'username': 'mary_student',
            'email': 'mary@lummyconsults.com',
            'first_name': 'Mary',
            'last_name': 'Johnson',
            'role': 'student',
            'password': 'password123'
        },
        {
            'username': 'tech_company',
            'email': 'hr@techcompany.com',
            'first_name': 'Tech',
            'last_name': 'Company',
            'role': 'employer',
            'password': 'password123'
        }
    ]
    
    for user_data in users_data:
        if not User.query.filter_by(username=user_data['username']).first():
            user = User(
                username=user_data['username'],
                email=user_data['email'],
                first_name=user_data['first_name'],
                last_name=user_data['last_name'],
                role=user_data['role']
            )
            user.set_password(user_data['password'])
            user.is_approved = True
            db.session.add(user)
    
    db.session.commit()
    print("Sample users created successfully!")
    
    # Create sample tutor profile
    tutor_user = User.query.filter_by(username='john_tutor').first()
    if tutor_user and not tutor_user.tutor_profile:
        tutor_profile = TutorProfile(
            user_id=tutor_user.id,
            qualification='B.Sc. Mathematics, M.Ed. Education',
            experience_years=5,
            subjects=json.dumps(['Mathematics', 'Physics', 'Chemistry']),
            teaching_levels=json.dumps(['Primary', 'Secondary', 'University']),
            location='Lagos, Nigeria',
            hourly_rate=5000.0,
            available_days=json.dumps(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']),
            available_times=json.dumps(['9:00-12:00', '14:00-17:00']),
            online_teaching=True,
            in_person_teaching=True,
            bio='Experienced mathematics tutor with 5+ years of teaching experience. Specializes in exam preparation for WAEC, NECO, and JAMB.'
        )
        db.session.add(tutor_profile)
    
    # Create sample student profile
    student_user = User.query.filter_by(username='mary_student').first()
    if student_user and not student_user.student_profile:
        student_profile = StudentProfile(
            user_id=student_user.id,
            current_level='Secondary',
            school='Lagos State Secondary School',
            subjects_of_interest=json.dumps(['Mathematics', 'Physics', 'Chemistry']),
            age=16,
            parent_contact='+234-xxx-xxx-xxxx',
            address='Lagos, Nigeria'
        )
        db.session.add(student_profile)
    
    # Create sample job posting
    employer_user = User.query.filter_by(username='tech_company').first()
    if employer_user:
        job_posting = JobPosting(
            employer_id=employer_user.id,
            title='Software Developer',
            description='We are looking for a skilled software developer to join our team.',
            requirements='Bachelor\'s degree in Computer Science or related field. 2+ years experience.',
            location='Lagos, Nigeria',
            job_type='full-time',
            salary_range='₦300,000 - ₦500,000',
            company_name='Tech Solutions Ltd',
            company_description='Leading technology company in Lagos.',
            application_deadline=datetime(2024, 12, 31),
            positions_available=2,
            status='active'
        )
        db.session.add(job_posting)
    
    # Create sample library item
    admin_user = User.query.filter_by(username='admin').first()
    if admin_user:
        library_item = LibraryItem(
            uploader_id=admin_user.id,
            title='Mathematics for Senior Secondary School',
            description='Comprehensive mathematics textbook for SS1-SS3 students.',
            category='textbook',
            subject='Mathematics',
            level='secondary',
            filename='math_textbook.pdf',
            file_type='pdf',
            file_size=1024000,
            price=2000.0,
            is_free=False,
            status='approved'
        )
        db.session.add(library_item)
    
    db.session.commit()
    print("Sample data created successfully!")

if __name__ == '__main__':
    # Create database tables
    with app.app_context():
        db.create_all()
    
    # Run the application
    app.run(
        debug=app.config.get('DEBUG', False),
        host='0.0.0.0',
        port=5000
    )

