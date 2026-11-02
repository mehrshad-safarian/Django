# Tehran Luxury Cars

**Live Demo:** [https://tehranluxurycars.blitz.cloud](https://tehranluxurycars.blitz.cloud)

A Django-based car marketplace focused on backend development, user management, vehicle listings, filtering, location data, image uploads, and email communication.

A practical project demonstrating real-world web application development using Django and its ecosystem.

---

## Features

- **User Accounts & Profiles:** User registration, authentication, and profile management using Django's built-in authentication system.
- **Vehicle Listings:** Create and manage vehicle listings with details such as brand, model, year, price, mileage, images, and location.
- **Ownership-Based Permissions:** Users can manage their own listings through ownership-based access control.
- **Listing Likes:** Users can like listings, with duplicate likes prevented through database relationships.
- **Filtering & Search:** Filter vehicle listings using `django-filter`.
- **Location Data:** Structured geographic information for vehicle listings.
- **UUID Identifiers:** UUID primary keys for important models instead of sequential integer IDs.
- **Email Inquiries:** Asynchronous seller inquiries using jQuery AJAX and Django SMTP integration.
- **CSRF Protection:** Secure AJAX requests using Django's built-in CSRF protection and server-side validation.
- **Django Signals:** Event-driven operations separated from views where appropriate.
- **Forms & Validation:** Django Forms and Model Forms for structured input handling and validation.
- **Customized Django Admin:** Improved management of users, listings, and application data.
- **Image Uploads:** Image processing with Pillow and separate static/media handling.
- **Responsive UI:** Responsive frontend built with Bootstrap 5.

---

## Tech Stack

| Category | Technology |
|---|---|
| Language | Python 3.13 |
| Backend | Django 6.0 |
| Database Layer | Django ORM |
| Authentication | Django Authentication |
| Filtering | django-filter |
| Forms | Django Forms / Model Forms |
| Localized Fields | django-localflavor |
| Image Processing | Pillow |
| Email | SMTP |
| Frontend | HTML, CSS, JavaScript |
| UI Framework | Bootstrap 5 |
| AJAX | jQuery |
| Production Server | Gunicorn |
| Static Files | WhiteNoise |
| Environment Variables | django-environ |

---

## Getting Started

### Requirements

- Python 3.13+
- Git
- A configured SMTP service

### Installation

Clone the repository:

```bash
git clone <repository-url>
cd <project-directory>
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it:

**Windows**
```bash
venv\Scripts\activate
```

**Linux / macOS**
```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Configure the required environment variables, then apply migrations:

```bash
python manage.py migrate
```

Run the development server:

```bash
python manage.py runserver
```

The application will be available at:

`http://127.0.0.1:8000/`

---

## Testing & QA

The project is reviewed for:

- Authentication & Authorization
- Form Validation
- CSRF Protection
- AJAX Requests
- Email Delivery
- Image Uploads
- Database Relationships
- Django Admin
- Error Handling
- Static & Media Configuration
- Production Settings

---

## Project Status

- Backend: **Complete**
- Frontend: **Complete**
- Core Features: **Complete**
- Production Audit: **In Progress**
- Deployment: **Complete**
- Public Release: **Complete**

---

## Project Goals

This project demonstrates practical experience in building a database-driven Django application, with an emphasis on backend architecture, authentication, database relationships, validation, asynchronous requests, email integration, file handling, and application management.

---

## Author

**Mehrshad**

Built with **Python & Django**.