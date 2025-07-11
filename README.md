# Lummy Consults - Multi-Service Educational Platform

![Lummy Consults Logo](app/static/images/lummy.jpg)

A comprehensive web application that provides tutoring services, recruitment solutions, and educational library resources. Built with Flask, featuring a modern, responsive design with family-friendly colors, smooth animations, and professional user experience.

## 🌟 Features

### 🎓 Tutoring Services

- **Student-Tutor Matching**: Connect students with qualified tutors across all subjects
- **Flexible Learning**: Support for both online and in-person sessions
- **Comprehensive Subjects**: Mathematics, Physics, Chemistry, English, French, Music, and more
- **Exam Preparation**: WAEC, NECO, JAMB, IGCSE, TOEFL, UTME support
- **All Age Groups**: From toddlers to university students
- **Online Learning Portal**: Track progress, schedule sessions, and communicate with tutors
- **Video Integration**: Ready for Jitsi Meet or Zoom integration

### 💼 Recruitment Services

- **Job Posting Platform**: Employers can post job openings
- **Candidate Matching**: Advanced matching system for jobs and candidates
- **Application Management**: Track applications and hiring progress
- **CV Management**: Upload and manage resumes
- **Interview Scheduling**: Built-in interview management system

### 📚 Educational Library

- **Digital Resources**: Upload and sell educational materials (PDF, DOC, etc.)
- **Content Management**: Admin approval system for uploaded content
- **Payment Integration**: Ready for Paystack, Flutterwave, or Stripe
- **Preview System**: Allow users to preview materials before purchase
- **Category Organization**: Organize by subject, level, and type

### 🛠 Admin Dashboard

- **Unified Control Panel**: Manage all services from one dashboard
- **User Management**: Approve tutors, manage user accounts
- **Content Moderation**: Review and approve library content
- **Analytics**: Track platform usage and performance
- **System Settings**: Configure platform settings and preferences

## 🚀 Technology Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **Database**: SQLAlchemy (SQLite for development, PostgreSQL/MySQL for production)
- **Authentication**: Flask-Login with role-based access control
- **Email**: Flask-Mail for notifications
- **File Upload**: Secure file handling and storage
- **Animations**: ScrollReveal.js for smooth scroll animations
- **Responsive Design**: Mobile-first approach

## 📁 Project Structure

```
lummy-consults/
├── app/
│   ├── __init__.py              # Application factory
│   ├── models.py                # Database models
│   ├── admin/                   # Admin dashboard
│   │   ├── __init__.py
│   │   └── routes.py
│   ├── auth/                    # Authentication
│   │   ├── __init__.py
│   │   └── routes.py
│   ├── library/                 # Educational library
│   │   ├── __init__.py
│   │   └── routes.py
│   ├── main/                    # Main application routes
│   │   ├── __init__.py
│   │   └── routes.py
│   ├── recruitment/             # Recruitment services
│   │   ├── __init__.py
│   │   └── routes.py
│   ├── tutors/                  # Tutoring services
│   │   ├── __init__.py
│   │   └── routes.py
│   ├── static/                  # Static files
│   │   ├── css/
│   │   │   └── style.css
│   │   ├── js/
│   │   │   └── main.js
│   │   └── images/
│   │       ├── lummy.jpg
│   │       └── ...
│   └── templates/               # HTML templates
│       ├── layout.html
│       ├── index.html
│       ├── auth/
│       │   ├── login.html
│       │   └── register.html
│       ├── tutors/
│       ├── recruitment/
│       ├── library/
│       └── admin/
├── migrations/                  # Database migrations
├── uploads/                     # User uploaded files
├── config.py                    # Configuration settings
├── requirements.txt             # Python dependencies
├── run.py                      # Application entry point
└── README.md                   # This file
```

## 🛠 Installation & Setup

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git (for version control)

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/lummy-consults.git
cd lummy-consults
```

### Step 2: Create Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Set Environment Variables

Create a `.env` file in the root directory:

```bash
SECRET_KEY=your-secret-key-here
FLASK_ENV=development
FLASK_DEBUG=True
DATABASE_URL=sqlite:///lummy_consults.db
```

### Step 5: Initialize Database

```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

### Step 6: Create Sample Data

```bash
flask create-sample-data
```

### Step 7: Run the Application

```bash
python run.py
```

The application will be available at `http://localhost:5000`

## 👥 Default User Accounts

After running the sample data creation command, you can login with:

- **Admin**: `admin` / `admin123`
- **Tutor**: `john_tutor` / `password123`
- **Student**: `mary_student` / `password123`
- **Employer**: `tech_company` / `password123`

## 🎨 Design Features

### Color Scheme

- **Primary Colors**: Deep purple (#6200EA), Teal (#03DAC5)
- **Secondary Colors**: Green (#4CAF50), Blue gradients
- **Background**: Warm whites and light grays
- **Accents**: Yellow highlights (#ffeb3b)

### Animations

- **Scroll Reveal**: Elements animate as you scroll
- **Hover Effects**: Interactive buttons and cards
- **Loading States**: Smooth transitions and loading indicators
- **Parallax Effects**: Hero section background movement
- **Counter Animation**: Statistics count up when in view

### Typography

- **Primary Font**: Arial (system font for reliability)
- **Headings**: Bold, large sizes for impact
- **Body Text**: Clean, readable font sizes
- **Responsive**: Scales appropriately on all devices

## 📱 Responsive Design

- **Mobile-First**: Optimized for mobile devices
- **Tablet-Friendly**: Adapts to tablet screen sizes
- **Desktop Enhanced**: Full features on desktop
- **Cross-Browser**: Compatible with modern browsers

## 🔧 Configuration

### Environment Variables

```bash
# Flask Configuration
SECRET_KEY=your-secret-key
FLASK_ENV=development|production
FLASK_DEBUG=True|False

# Database
DATABASE_URL=sqlite:///lummy_consults.db

# Email Configuration
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USE_TLS=true
MAIL_USERNAME=your-email@gmail.com
MAIL_PASSWORD=your-app-password

# Payment Gateways
PAYSTACK_PUBLIC_KEY=pk_test_...
PAYSTACK_SECRET_KEY=sk_test_...
FLUTTERWAVE_PUBLIC_KEY=FLWPUBK_TEST-...
FLUTTERWAVE_SECRET_KEY=FLWSECK_TEST-...
```

### Database Models

#### User Management

- `User`: Base user model with roles
- `TutorProfile`: Extended profile for tutors
- `StudentProfile`: Extended profile for students

#### Tutoring System

- `TutorBooking`: Session bookings and scheduling
- `TutorReview`: Ratings and feedback

#### Recruitment System

- `JobPosting`: Job listings
- `JobApplication`: Application tracking

#### Library System

- `LibraryItem`: Educational materials
- `LibraryPurchase`: Purchase tracking

#### General

- `ContactMessage`: Contact form submissions
- `Testimonial`: Customer testimonials
- `AuditLog`: System activity tracking

## 🚀 Deployment

### Production Deployment

1. **Update Configuration**

   ```python
   # config.py
   class ProductionConfig(Config):
       DEBUG = False
       SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
   ```

2. **Set Environment Variables**

   ```bash
   export FLASK_ENV=production
   export DATABASE_URL=postgresql://user:pass@localhost/lummy_consults
   ```

3. **Use Production Server**
   ```bash
   gunicorn -w 4 -b 0.0.0.0:5000 run:app
   ```

### Heroku Deployment

1. **Create Heroku App**

   ```bash
   heroku create lummy-consults
   ```

2. **Add Database**

   ```bash
   heroku addons:create heroku-postgresql:hobby-dev
   ```

3. **Deploy**
   ```bash
   git push heroku main
   heroku run flask db upgrade
   heroku run flask create-sample-data
   ```

## 🔐 Security Features

- **Password Hashing**: Werkzeug password hashing
- **CSRF Protection**: Flask-WTF CSRF tokens
- **SQL Injection Prevention**: SQLAlchemy ORM
- **File Upload Security**: Secure file handling
- **Role-Based Access**: User role management
- **Session Management**: Secure session handling

## 📚 API Documentation

### Authentication Endpoints

- `POST /auth/login`: User login
- `POST /auth/register`: User registration
- `GET /auth/logout`: User logout

### Tutoring Endpoints

- `GET /tutors`: List all tutors
- `GET /tutors/<id>`: Get tutor details
- `POST /tutors/book`: Book a session

### Recruitment Endpoints

- `GET /recruitment/jobs`: List job postings
- `GET /recruitment/job/<id>`: Get job details
- `POST /recruitment/apply`: Apply for job

### Library Endpoints

- `GET /library`: List library items
- `GET /library/item/<id>`: Get item details
- `POST /library/purchase`: Purchase item

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📞 Contact

- **Company**: Lummy Consults
- **Location**: Lagos, Nigeria
- **Email**: info@lummyconsults.com
- **Facebook**: [@lummytutors](https://facebook.com/lummytutors)
- **Instagram**: [@lummy_tutors](https://instagram.com/lummy_tutors)
- **Google**: [Lummy Consults](https://google.com/lummytutors)

## 🙏 Acknowledgments

- Flask community for excellent documentation
- ScrollReveal.js for smooth animations
- All contributors and testers
- The Nigerian education community

---

**Made with ❤️ for the Nigerian education community**
