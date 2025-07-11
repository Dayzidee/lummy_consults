from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app import db, login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin, db.Model):
    """User model for authentication across all modules"""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(120), nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(20))
    
    # User roles: 'student', 'tutor', 'employer', 'job_seeker', 'admin'
    role = db.Column(db.String(20), nullable=False, default='student')
    is_active = db.Column(db.Boolean, default=True)
    is_approved = db.Column(db.Boolean, default=False)  # For tutors and admin approval
    
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    tutor_profile = db.relationship('TutorProfile', backref='user', uselist=False)
    student_profile = db.relationship('StudentProfile', backref='user', uselist=False)
    job_applications = db.relationship('JobApplication', backref='applicant', lazy='dynamic')
    library_purchases = db.relationship('LibraryPurchase', backref='user', lazy='dynamic')
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def __repr__(self):
        return f'<User {self.username}>'

class TutorProfile(db.Model):
    """Extended profile for tutors"""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    # Professional information
    qualification = db.Column(db.Text)
    experience_years = db.Column(db.Integer)
    subjects = db.Column(db.Text)  # JSON string of subjects
    teaching_levels = db.Column(db.Text)  # JSON string of levels (primary, secondary, etc.)
    location = db.Column(db.String(100))
    hourly_rate = db.Column(db.Float)
    
    # Availability
    available_days = db.Column(db.Text)  # JSON string of available days
    available_times = db.Column(db.Text)  # JSON string of time slots
    
    # Teaching preferences
    online_teaching = db.Column(db.Boolean, default=True)
    in_person_teaching = db.Column(db.Boolean, default=True)
    
    # Profile details
    bio = db.Column(db.Text)
    profile_picture = db.Column(db.String(200))
    
    # Ratings and reviews
    rating = db.Column(db.Float, default=0.0)
    total_reviews = db.Column(db.Integer, default=0)
    
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationships
    bookings = db.relationship('TutorBooking', backref='tutor', lazy='dynamic')
    
    def __repr__(self):
        return f'<TutorProfile {self.user.username}>'

class StudentProfile(db.Model):
    """Extended profile for students"""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    # Academic information
    current_level = db.Column(db.String(50))  # primary, secondary, university
    school = db.Column(db.String(100))
    subjects_of_interest = db.Column(db.Text)  # JSON string
    
    # Personal information
    age = db.Column(db.Integer)
    parent_contact = db.Column(db.String(20))
    address = db.Column(db.Text)
    
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationships
    bookings = db.relationship('TutorBooking', backref='student', lazy='dynamic')
    
    def __repr__(self):
        return f'<StudentProfile {self.user.username}>'

class TutorBooking(db.Model):
    """Booking system for tutor sessions"""
    id = db.Column(db.Integer, primary_key=True)
    tutor_id = db.Column(db.Integer, db.ForeignKey('tutor_profile.id'), nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey('student_profile.id'), nullable=False)
    
    # Session details
    subject = db.Column(db.String(100), nullable=False)
    session_type = db.Column(db.String(20), nullable=False)  # 'online' or 'in_person'
    scheduled_date = db.Column(db.DateTime, nullable=False)
    duration_minutes = db.Column(db.Integer, default=60)
    
    # Status: 'pending', 'confirmed', 'completed', 'cancelled'
    status = db.Column(db.String(20), default='pending')
    
    # Payment information
    cost = db.Column(db.Float)
    payment_status = db.Column(db.String(20), default='pending')  # 'pending', 'paid', 'refunded'
    
    # Session notes
    session_notes = db.Column(db.Text)
    student_feedback = db.Column(db.Text)
    tutor_feedback = db.Column(db.Text)
    rating = db.Column(db.Integer)  # 1-5 rating
    
    # Online session details
    meeting_link = db.Column(db.String(200))
    meeting_id = db.Column(db.String(50))
    
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def __repr__(self):
        return f'<TutorBooking {self.id}>'

class JobPosting(db.Model):
    """Job postings for recruitment module"""
    id = db.Column(db.Integer, primary_key=True)
    employer_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    # Job details
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    requirements = db.Column(db.Text)
    location = db.Column(db.String(100))
    job_type = db.Column(db.String(50))  # 'full-time', 'part-time', 'contract'
    salary_range = db.Column(db.String(100))
    
    # Company information
    company_name = db.Column(db.String(100), nullable=False)
    company_description = db.Column(db.Text)
    
    # Application settings
    application_deadline = db.Column(db.DateTime)
    positions_available = db.Column(db.Integer, default=1)
    
    # Status: 'active', 'closed', 'pending_approval'
    status = db.Column(db.String(20), default='pending_approval')
    
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    employer = db.relationship('User', backref='job_postings')
    applications = db.relationship('JobApplication', backref='job', lazy='dynamic')
    
    def __repr__(self):
        return f'<JobPosting {self.title}>'

class JobApplication(db.Model):
    """Job applications from job seekers"""
    id = db.Column(db.Integer, primary_key=True)
    job_id = db.Column(db.Integer, db.ForeignKey('job_posting.id'), nullable=False)
    applicant_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    # Application details
    cover_letter = db.Column(db.Text)
    cv_filename = db.Column(db.String(200))
    
    # Status: 'pending', 'reviewed', 'shortlisted', 'interviewed', 'hired', 'rejected'
    status = db.Column(db.String(20), default='pending')
    
    # Interview details
    interview_date = db.Column(db.DateTime)
    interview_notes = db.Column(db.Text)
    
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def __repr__(self):
        return f'<JobApplication {self.id}>'

class LibraryItem(db.Model):
    """Educational materials in the library"""
    id = db.Column(db.Integer, primary_key=True)
    uploader_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    # Item details
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    category = db.Column(db.String(100))  # 'textbook', 'notes', 'past_questions', etc.
    subject = db.Column(db.String(100))
    level = db.Column(db.String(50))  # 'primary', 'secondary', 'university'
    
    # File information
    filename = db.Column(db.String(200), nullable=False)
    file_type = db.Column(db.String(20), nullable=False)  # 'pdf', 'doc', etc.
    file_size = db.Column(db.Integer)  # in bytes
    
    # Pricing and sales
    price = db.Column(db.Float, nullable=False)
    is_free = db.Column(db.Boolean, default=False)
    
    # Preview information
    preview_filename = db.Column(db.String(200))  # For preview file
    preview_pages = db.Column(db.Integer, default=3)
    
    # Status: 'pending', 'approved', 'rejected'
    status = db.Column(db.String(20), default='pending')
    
    # Statistics
    download_count = db.Column(db.Integer, default=0)
    rating = db.Column(db.Float, default=0.0)
    total_reviews = db.Column(db.Integer, default=0)
    
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    uploader = db.relationship('User', backref='library_uploads')
    purchases = db.relationship('LibraryPurchase', backref='item', lazy='dynamic')
    
    def __repr__(self):
        return f'<LibraryItem {self.title}>'

class LibraryPurchase(db.Model):
    """Track library item purchases"""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    item_id = db.Column(db.Integer, db.ForeignKey('library_item.id'), nullable=False)
    
    # Purchase details
    purchase_price = db.Column(db.Float, nullable=False)
    payment_method = db.Column(db.String(50))  # 'paystack', 'flutterwave', etc.
    transaction_id = db.Column(db.String(100))
    
    # Status: 'pending', 'completed', 'failed', 'refunded'
    payment_status = db.Column(db.String(20), default='pending')
    
    # Download tracking
    download_count = db.Column(db.Integer, default=0)
    last_downloaded = db.Column(db.DateTime)
    
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<LibraryPurchase {self.id}>'

class ContactMessage(db.Model):
    """Contact form messages"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(20))
    subject = db.Column(db.String(200))
    message = db.Column(db.Text, nullable=False)
    
    # Status: 'new', 'read', 'replied'
    status = db.Column(db.String(20), default='new')
    
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<ContactMessage {self.name}>'

class Testimonial(db.Model):
    """Customer testimonials"""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
    # Testimonial details
    name = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(100))  # 'Student', 'Parent', 'Employer', etc.
    company = db.Column(db.String(100))
    testimonial = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Integer, default=5)  # 1-5 stars
    
    # Display settings
    is_featured = db.Column(db.Boolean, default=False)
    is_approved = db.Column(db.Boolean, default=False)
    
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationships
    user = db.relationship('User', backref='testimonials')
    
    def __repr__(self):
        return f'<Testimonial {self.name}>'

class SystemSettings(db.Model):
    """System configuration settings"""
    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(100), unique=True, nullable=False)
    value = db.Column(db.Text)
    description = db.Column(db.Text)
    
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def __repr__(self):
        return f'<SystemSettings {self.key}>'

class AuditLog(db.Model):
    """Audit log for important system actions"""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    action = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    ip_address = db.Column(db.String(45))
    user_agent = db.Column(db.Text)
    
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationships
    user = db.relationship('User', backref='audit_logs')
    
    def __repr__(self):
        return f'<AuditLog {self.action}>'

