import os
from datetime import timedelta

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    """Base configuration class with common settings"""
    
    # Flask app settings
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'lummy-consults-secret-key-2024'
    
    # Database configuration
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'lummy_consults.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Mail settings (for contact forms and notifications)
    MAIL_SERVER = os.environ.get('MAIL_SERVER') or 'smtp.gmail.com'
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 587)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', 'true').lower() in ['true', 'on', '1']
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME') or 'lummyconsults@gmail.com'
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') or 'your-app-password'
    
    # File upload settings
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max file size
    UPLOAD_FOLDER = os.path.join(basedir, 'uploads')
    ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'doc', 'docx', 'ppt', 'pptx'}
    
    # Session settings
    PERMANENT_SESSION_LIFETIME = timedelta(hours=2)
    
    # Payment gateway settings (placeholders)
    PAYSTACK_PUBLIC_KEY = os.environ.get('PAYSTACK_PUBLIC_KEY') or 'pk_test_placeholder'
    PAYSTACK_SECRET_KEY = os.environ.get('PAYSTACK_SECRET_KEY') or 'sk_test_placeholder'
    FLUTTERWAVE_PUBLIC_KEY = os.environ.get('FLUTTERWAVE_PUBLIC_KEY') or 'FLWPUBK_TEST-placeholder'
    FLUTTERWAVE_SECRET_KEY = os.environ.get('FLUTTERWAVE_SECRET_KEY') or 'FLWSECK_TEST-placeholder'
    
    # Video conferencing settings
    JITSI_DOMAIN = 'meet.jit.si'
    ZOOM_API_KEY = os.environ.get('ZOOM_API_KEY') or 'zoom_api_placeholder'
    ZOOM_API_SECRET = os.environ.get('ZOOM_API_SECRET') or 'zoom_secret_placeholder'
    
    # Social media links
    FACEBOOK_URL = 'https://facebook.com/lummytutors'
    INSTAGRAM_URL = 'https://instagram.com/lummy_tutors'
    GOOGLE_MAPS_URL = 'https://www.google.com/maps/place/Lummy+Consults/@6.5741786,3.4011417,17z/data=!3m1!4b1!4m6!3m5!1s0x103b93a27a21447d:0xa863cba77156f9a5!8m2!3d6.5741786!4d3.4011417!16s%2Fg%2F11s7d488_f?entry=ttu&g_ep=EgoyMDI1MDcwNi4wIKXMDSoASAFQAw%3D%3D'
    
    # Company information
    COMPANY_NAME = 'Lummy Consults'
    COMPANY_ADDRESS = 'Lagos, Nigeria'
    COMPANY_PHONE = '+234-xxx-xxx-xxxx'
    COMPANY_EMAIL = 'info@lummyconsults.com'
    
    # Pagination settings
    POSTS_PER_PAGE = 10
    TUTORS_PER_PAGE = 12
    JOBS_PER_PAGE = 15
    LIBRARY_ITEMS_PER_PAGE = 20

class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True
    SQLALCHEMY_ECHO = True

class ProductionConfig(Config):
    """Production configuration"""
    DEBUG = False
    SQLALCHEMY_ECHO = False

class TestingConfig(Config):
    """Testing configuration"""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
    WTF_CSRF_ENABLED = False

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}

