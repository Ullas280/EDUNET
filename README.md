# 💼 EDUNET Job Portal

A modern, full-stack Job Portal application enabling seamless connection between job seekers and recruiters. Built with React.js frontend and Django REST backend, featuring a clean, responsive UI with smooth animations.

[![GitHub Repository](https://img.shields.io/badge/GitHub-EDUNET-blue?logo=github)](https://github.com/Ullas280/EDUNET)
[![Django](https://img.shields.io/badge/Django-4.2+-green?logo=django)](https://www.djangoproject.com/)
[![React](https://img.shields.io/badge/React-19.0+-blue?logo=react)](https://reactjs.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## 📋 Table of Contents

- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Prerequisites](#-prerequisites)
- [Installation & Setup](#-installation--setup)
- [Environment Variables](#-environment-variables)
- [Running the Application](#-running-the-application)
- [API Documentation](#-api-documentation)
- [Architecture](#-architecture)
- [Contributing](#-contributing)
- [License](#-license)

---

## ✨ Features

### 🔐 Authentication & Authorization
- Secure JWT-based authentication system
- Role-based access control (Student/Recruiter)
- HTTP-only cookie storage for enhanced security
- Protected routes and API endpoints

### 🎓 Student Features
- Browse and search job listings with filters
- Apply to jobs with one-click application
- Track application status in personal dashboard
- View company profiles and job details
- Update profile with resume and skills

### 🧑‍💼 Recruiter Features
- Post new job opportunities
- View and manage all applicants
- Edit or delete job postings
- Company profile management
- Application status tracking
- Dashboard with analytics

### 🎨 User Interface
- Modern, responsive design built with Tailwind CSS
- Beautiful UI components using shadcn/ui
- Smooth animations with Framer Motion
- Mobile-first approach
- Consistent and accessible component design
- Dark mode ready

---

## 🛠️ Tech Stack

### Frontend
- **React.js 19** - Component-based UI library
- **Vite** - Fast build tool and dev server
- **Tailwind CSS 4** - Utility-first CSS framework
- **shadcn/ui** - Headless UI component library
- **Framer Motion** - Animation library
- **Redux Toolkit** - State management
- **React Router DOM 7** - Client-side routing
- **Axios** - HTTP client for API calls
- **Lucide React** - Icon library

### Backend
- **Django 4.2+** - Python web framework
- **Django REST Framework** - RESTful API toolkit
- **Simple JWT** - JWT authentication
- **MySQL** - Relational database
- **PyMySQL** - MySQL client library
- **Cloudinary** - Media storage and CDN
- **CORS Headers** - Cross-origin resource sharing

### Development Tools
- **ESLint** - JavaScript linting
- **Vite** - Frontend build tool
- **Git** - Version control

---

## 📁 Project Structure

```
EDUNET/
├── job-portal-main/
│   ├── Client/                      # React Frontend Application
│   │   ├── public/                  # Static assets
│   │   ├── src/
│   │   │   ├── assets/              # Images, icons
│   │   │   ├── components/          # React components
│   │   │   │   ├── admin/           # Recruiter dashboard components
│   │   │   │   ├── auth/            # Authentication components
│   │   │   │   ├── shared/          # Shared/common components
│   │   │   │   └── ui/              # shadcn/ui components
│   │   │   ├── hooks/               # Custom React hooks
│   │   │   ├── redux/               # Redux store and slices
│   │   │   ├── utils/               # Utility functions & constants
│   │   │   ├── App.jsx              # Main app component
│   │   │   └── main.jsx             # Entry point
│   │   ├── package.json             # Frontend dependencies
│   │   ├── vite.config.js           # Vite configuration
│   │   └── tailwind.config.js       # Tailwind CSS config
│   │
│   ├── server_django/               # Django Backend Application
│   │   ├── accounts/                # User authentication app
│   │   │   ├── models.py            # User model
│   │   │   ├── serializers.py       # User serializers
│   │   │   ├── views.py             # Auth views
│   │   │   └── urls.py              # Auth routes
│   │   ├── jobs/                    # Jobs & applications app
│   │   │   ├── models.py            # Job, Company, Application models
│   │   │   ├── serializers.py       # Job serializers
│   │   │   ├── views.py             # Job views
│   │   │   └── urls.py              # Job routes
│   │   ├── job_portal_django/       # Project settings
│   │   │   ├── settings.py          # Django settings
│   │   │   ├── urls.py              # Main URL configuration
│   │   │   └── cookie_auth.py       # Custom JWT authentication
│   │   ├── manage.py                # Django management script
│   │   ├── requirements.txt         # Python dependencies
│   │   ├── docker-compose.yml       # Docker MySQL setup
│   │   └── README.md                # Backend documentation
│   │
│   └── archive/                     # Archived Node.js backend
│       └── server_node_backup_*/    # Previous Express backend
│
├── server_django/                   # Backend test scripts
│   ├── e2e_test.ps1                # End-to-end tests
│   └── logout_test.ps1             # Logout testing
│
└── README.md                        # This file
```

---

## 📋 Prerequisites

Before you begin, ensure you have the following installed:

- **Node.js** (v18 or higher) - [Download](https://nodejs.org/)
- **Python** (v3.9 or higher) - [Download](https://www.python.org/)
- **MySQL** (v8.0 or higher) - [Download](https://www.mysql.com/) or use Docker
- **Git** - [Download](https://git-scm.com/)
- **npm** or **yarn** - Package manager for Node.js
- **pip** - Python package manager

---

## 🚀 Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Ullas280/EDUNET.git
cd EDUNET
```

### 2. Backend Setup (Django)

```bash
# Navigate to Django backend
cd job-portal-main/server_django

# Create virtual environment
python -m venv .venv

# Activate virtual environment
# Windows PowerShell:
.\.venv\Scripts\Activate.ps1
# Windows CMD:
.venv\Scripts\activate.bat
# Linux/Mac:
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Setup MySQL Database (Option 1: Docker)
docker-compose up -d

# OR Setup MySQL Database (Option 2: Manual)
# Create a MySQL database named 'job_portal'
# Update credentials in .env file

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Create superuser (optional)
python manage.py createsuperuser

# Load initial data (optional)
# python manage.py loaddata initial_data.json
```

### 3. Frontend Setup (React)

```bash
# Navigate to React frontend
cd ../Client

# Install dependencies
npm install

# Create .env file for frontend (see Environment Variables section)
```

---

## 🔐 Environment Variables

### Backend (.env) - `server_django/.env`

Create a `.env` file in the `server_django/` directory:

```env
# Django Settings
SECRET_KEY=your-django-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Database Configuration
DB_ENGINE=django.db.backends.mysql
DB_NAME=job_portal
DB_USER=root
DB_PASSWORD=your_mysql_password
DB_HOST=localhost
DB_PORT=3306

# JWT Settings
JWT_ACCESS_TOKEN_LIFETIME=60  # minutes
JWT_REFRESH_TOKEN_LIFETIME=1  # days

# Cloudinary Configuration (for image uploads)
CLOUDINARY_CLOUD_NAME=your_cloud_name
CLOUDINARY_API_KEY=your_api_key
CLOUDINARY_API_SECRET=your_api_secret

# CORS Settings
CORS_ALLOWED_ORIGINS=http://localhost:5173,http://localhost:3000
```

### Frontend (.env) - `Client/.env`

Create a `.env` file in the `Client/` directory:

```env
# Backend API URL
VITE_BACKEND_URL=http://localhost:8000
```

---

## 🏃 Running the Application

### Start Backend Server

```bash
# Navigate to backend directory
cd job-portal-main/server_django

# Activate virtual environment
.\.venv\Scripts\Activate.ps1  # Windows PowerShell

# Run Django development server
python manage.py runserver 8000
```

Backend will be available at: **http://localhost:8000**

### Start Frontend Development Server

```bash
# Open a new terminal
# Navigate to frontend directory
cd job-portal-main/Client

# Start Vite development server
npm run dev
```

Frontend will be available at: **http://localhost:5173**

### Access the Application

- **Frontend**: http://localhost:5173
- **Backend API**: http://localhost:8000/api/v1/
- **Django Admin**: http://localhost:8000/admin/

---

## 📡 API Documentation

### Base URL
```
http://localhost:8000/api/v1
```

### Authentication Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/user/register` | Register new user |
| POST | `/user/login` | Login user (sets JWT cookie) |
| POST | `/user/logout` | Logout user (clears cookie) |
| GET | `/user/profile` | Get user profile |
| PUT | `/user/profile/update` | Update user profile |

### Job Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/job/` | Get all jobs (with filters) |
| GET | `/job/:id` | Get job by ID |
| POST | `/job/post` | Post new job (Recruiter) |
| PUT | `/job/:id` | Update job (Recruiter) |
| DELETE | `/job/:id` | Delete job (Recruiter) |
| GET | `/job/admin/jobs` | Get recruiter's jobs |

### Company Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/company/` | Get all companies |
| GET | `/company/:id` | Get company by ID |
| POST | `/company/register` | Register company (Recruiter) |
| PUT | `/company/:id` | Update company (Recruiter) |

### Application Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/application/apply/:id` | Apply to job (Student) |
| GET | `/application/get` | Get user's applications |
| GET | `/application/:id/applicants` | Get job applicants (Recruiter) |
| PUT | `/application/status/:id/update` | Update application status |

### Request Examples

**Register User:**
```bash
POST /api/v1/user/register
Content-Type: application/json

{
  "fullname": "John Doe",
  "email": "john@example.com",
  "phoneNumber": "1234567890",
  "password": "securepassword",
  "role": "student"  // or "recruiter"
}
```

**Login User:**
```bash
POST /api/v1/user/login
Content-Type: application/json

{
  "email": "john@example.com",
  "password": "securepassword",
  "role": "student"
}
```

---

## 🏗️ Architecture

### Authentication Flow
1. User registers/logs in via frontend
2. Backend validates credentials
3. JWT token generated and stored in HTTP-only cookie
4. Frontend makes authenticated requests with cookie
5. Backend validates JWT token on each request

### State Management
- **Redux Toolkit** for global state
- **Redux Persist** for state persistence
- Slices: `authSlice`, `jobSlice`, `companySlice`, `applicationSlice`

### API Communication
- Axios instance configured with base URL
- Interceptors for request/response handling
- Cookie-based authentication
- Error handling and logging

---

## 🔧 Development

### Backend Development

```bash
# Run tests
python manage.py test

# Create new app
python manage.py startapp app_name

# Make migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Django shell
python manage.py shell
```

### Frontend Development

```bash
# Run development server
npm run dev

# Build for production
npm run build

# Preview production build
npm run preview

# Run linter
npm run lint
```

---

## 🧪 Testing

### Backend Tests

```powershell
# Run all tests
python manage.py test

# Run specific test
python manage.py test accounts.tests.test_views

# Run with coverage
coverage run --source='.' manage.py test
coverage report
```

### End-to-End Tests

```powershell
# Run E2E tests
.\server_django\e2e_test.ps1

# Run logout tests
.\server_django\logout_test.ps1
```

---

## 📦 Deployment

### Frontend Deployment (Vercel)

1. Push code to GitHub
2. Connect repository to Vercel
3. Configure environment variables
4. Deploy

### Backend Deployment (Railway/Heroku/AWS)

1. Configure production settings
2. Set up production database
3. Configure environment variables
4. Deploy using platform-specific CLI

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👥 Authors

- **Ullas280** - *Project Owner* - [GitHub](https://github.com/Ullas280)
- **Contributors** - See [Contributors](https://github.com/Ullas280/EDUNET/graphs/contributors)

---

## 🙏 Acknowledgments

- Original template by [Shubham Kumar](https://github.com/shubham79a)
- shadcn/ui for beautiful components
- Tailwind CSS for styling utilities
- Django REST Framework community
- React and Vite teams

---

## 📞 Support

For support, email support@edunet.com or open an issue in the GitHub repository.

---

## 🗺️ Roadmap

- [ ] Real-time notifications
- [ ] Chat feature between recruiter and applicant
- [ ] Advanced search filters
- [ ] Resume parser
- [ ] Email notifications
- [ ] Analytics dashboard
- [ ] Mobile app (React Native)
- [ ] Multi-language support

---

## ⚠️ Important Notes

1. **Database**: MySQL is required. Use Docker Compose or install manually.
2. **Environment Variables**: Create `.env` files for both frontend and backend.
3. **Cloudinary**: Required for image uploads. Create a free account at [cloudinary.com](https://cloudinary.com/).
4. **CORS**: Ensure CORS settings allow your frontend URL.
5. **Python Version**: Python 3.9+ required for Django 4.2+.

---

**Made with ❤️ for EDUNET Job Portal Project**
