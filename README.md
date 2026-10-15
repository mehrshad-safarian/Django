# Tehran Luxury Cars
**Live Demo:** https://tehranluxurycars.blitz.cloud

یک مارکت‌پلیس خودرو با **Django** که با تمرکز بر توسعه‌ی بک‌اند، مدیریت کاربران، ثبت و مدیریت آگهی خودرو، فیلترینگ، اطلاعات مکانی، آپلود تصاویر و ارتباط از طریق ایمیل طراحی شده است.

> یک پروژه‌ی عملی برای نمایش توانایی توسعه‌ی یک وب‌اپلیکیشن کامل با Django و پیاده‌سازی قابلیت‌های واقعی سمت بک‌اند.

## ✨ قابلیت‌ها

### 👤 کاربران و پروفایل‌ها

کاربران می‌توانند در سیستم ثبت‌نام کرده و حساب کاربری و اطلاعات پروفایل خود را مدیریت کنند. احراز هویت و کنترل دسترسی با سیستم Authentication خود Django انجام می‌شود و اطلاعات مرتبط با پروفایل از اطلاعات اصلی کاربر جدا نگه داشته می‌شود .

### 🚘 آگهی‌های خودرو

کاربران احراز هویت‌شده می‌توانند آگهی خودرو ایجاد و مدیریت کنند. هر آگهی شامل اطلاعاتی مانند برند، مدل، سال ساخت، قیمت، کارکرد، توضیحات، اطلاعات تماس، تصاویر و موقعیت مکانی است.

هر آگهی به صاحب آن متصل است و دسترسی‌های مبتنی بر مالکیت مشخص می‌کنند چه کسی می‌تواند آگهی را ویرایش یا مدیریت کند.

### ❤️ لایک آگهی‌ها

کاربران می‌توانند آگهی‌های موردنظر خود را Like کنند. ارتباط بین کاربر و آگهی به‌صورت مجزا ذخیره می‌شود تا یک کاربر نتواند یک آگهی را چندین بار Like کند.

### 🔎 فیلتر و جست‌وجو

سیستم فیلترینگ با استفاده از **django-filter** پیاده‌سازی شده است تا کاربران بتوانند آگهی‌ها را بر اساس ویژگی‌های مختلف محدود کرده و سریع‌تر به خودروهای موردنظر خود برسند.

### 📍 اطلاعات مکانی

آگهی‌ها از اطلاعات مکانی ساختاریافته پشتیبانی می‌کنند و می‌توانند به یک موقعیت جغرافیایی مشخص مرتبط شوند. این ساختار امکان توسعه‌ی قابلیت‌های Location-Based در آینده را نیز فراهم می‌کند.

### 🆔 شناسه‌های UUID

برای شناسه‌ی مدل‌های مهم از **UUID** به‌جای شناسه‌های عددی ترتیبی استفاده شده است. این کار باعث می‌شود شناسه‌های عمومی قابل پیش‌بینی نباشند و برای مدل‌هایی که ID آن‌ها در URL یا درخواست‌های سمت کلاینت قرار می‌گیرد، مناسب‌تر باشند.

### 📧 ارسال درخواست از طریق ایمیل

کاربر می‌تواند از صفحه‌ی هر آگهی برای فروشنده درخواست ارسال کند. این درخواست با استفاده از **jQuery AJAX** به‌صورت Asynchronous ارسال می‌شود و Django مسئول پردازش درخواست، Validation، CSRF Protection و ارسال ایمیل از طریق SMTP است.

وضعیت درخواست نیز در Frontend مدیریت می‌شود تا کاربر هنگام ارسال ایمیل بازخورد مناسبی دریافت کند.

### 🛡️ محافظت از درخواست‌ها و CSRF

درخواست‌های AJAX از سیستم CSRF Protection خود Django استفاده می‌کنند و مکانیزم‌های امنیتی Django دور زده نمی‌شوند. داده‌های ارسال‌شده نیز در سمت سرور Validation می‌شوند تا درخواست‌های نامعتبر قبل از پردازش کنترل شوند.

### 🧩 Django Signals

در بخش‌هایی که تغییرات مربوط به مدل نیاز به اجرای خودکار عملیات دیگری دارند، از **Django Signals** استفاده شده است. این کار اجازه می‌دهد بخشی از منطق مرتبط با رویدادهای مدل از Viewها جدا باقی بماند.

### 📝 Django Forms و Model Forms

برای دریافت، پردازش و Validation داده‌های ورودی از **Django Forms** و **Model Forms** استفاده شده است. این ساختار باعث می‌شود Validation داده‌ها در لایه‌ی مناسب انجام شود و Viewها بیش از حد درگیر پردازش فرم نباشند.

### 🎛️ پنل مدیریت سفارشی Django

پنل Django Admin برای مدیریت بهتر کاربران، آگهی‌ها و داده‌های مرتبط سفارشی‌سازی شده است تا اطلاعات مهم و عملیات مدیریتی بدون نیاز به دسترسی مستقیم به دیتابیس قابل مدیریت باشند.

### 🖼️ آپلود تصاویر

آگهی‌های خودرو از آپلود تصویر پشتیبانی می‌کنند. تصاویر با استفاده از **Pillow** پردازش شده و فایل‌های Media از فایل‌های Static پروژه جدا نگه داشته می‌شوند.

### 📱 رابط کاربری Responsive

Frontend با استفاده از **Bootstrap 5** ساخته شده تا صفحات و جریان‌های اصلی کار با آگهی‌ها در اندازه‌های مختلف صفحه‌نمایش قابل استفاده باشند.

## ⚙️ Backend

Backend بر پایه‌ی Django ORM و معماری Model-View-Form ساخته شده است.

مفاهیم اصلی استفاده‌شده در Backend:

- Django ORM
- روابط بین مدل‌ها
- UUID Primary Keys
- Django Authentication
- Django Forms و Model Forms
- Django Signals
- django-filter
- Server-Side Validation
- CSRF Protection
- Image و Media Handling
- SMTP Email Integration
- Customized Django Admin

تمرکز اصلی پروژه روی Backend است و تلاش شده قابلیت‌ها با استفاده از امکانات اصلی Django و اکوسیستم آن پیاده‌سازی شوند.

## 🧰 تکنولوژی‌ها

| دسته | تکنولوژی |
|---|---|
| زبان | Python |
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

## 🚀 راه‌اندازی پروژه

### پیش‌نیازها

- Python 3.13+
- Git
- یک SMTP Service برای ارسال ایمیل

### نصب

```bash
git clone <repository-url>
cd <project-directory>

python -m venv venv
```

فعال‌سازی Virtual Environment:

**Windows**
```bash
venv\Scripts\activate
```

**Linux / macOS**
```bash
source venv/bin/activate
```

نصب Dependencies:

```bash
pip install -r requirements.txt
```

پس از تنظیم Environment Variables، Migrationها را اجرا کنید:

```bash
python manage.py migrate
```

اجرای Development Server:

```bash
python manage.py runserver
```

سپس پروژه از طریق آدرس زیر در دسترس خواهد بود:

```text
http://127.0.0.1:8000/
```

## 🧪 تست و بررسی

پروژه از نظر موارد زیر بررسی می‌شود:

- Authentication و Authorization
- Form Validation
- CSRF Protection
- AJAX Requests
- Email Delivery
- Image Uploads
- Database Relationships
- Django Admin
- Error Handling
- Static و Media Configuration
- Production Settings

## 📸 Screenshots

Screenshots صفحات اصلی و جریان‌های مهم پروژه در این بخش قرار خواهند گرفت.

## 📌 وضعیت پروژه

- Backend: **Complete**
- Frontend: **Complete**
- Core Features: **Complete**
- Production Audit: **In Progress**
- Deployment: **Planned**
- Public Release: **Planned**

## 🎯 هدف پروژه

این پروژه به‌عنوان یک پروژه‌ی عملی Django توسعه داده شده تا تجربه‌ی کار با یک Web Application واقعی و Database-Driven را نشان دهد.

تمرکز اصلی پروژه روی Django، طراحی مدل‌های دیتابیس، Authentication، Validation، درخواست‌های Asynchronous، Email Integration، File Handling، Filtering و مدیریت داده‌ها از طریق Django Admin است.

## 👨‍💻 توسعه‌دهنده

**Mehrshad**

Built with **Python & Django**.

---

# Tehran Luxury Cars

A full-stack car marketplace built with **Django**, focused on backend development, user management, vehicle listings, filtering, location data, image uploads, and email-based communication.

> A practical project demonstrating real-world web application development with Django and its core ecosystem.

## ✨ Features

### 👤 User Accounts & Profiles

Users can register, authenticate, and manage their accounts and profile information. Authentication and access control are handled using Django's built-in authentication system, while profile-related data is kept separate where needed.

### 🚘 Vehicle Listings

Authenticated users can create and manage vehicle listings containing information such as brand, model, year, price, mileage, description, contact information, images, and location.

Each listing is associated with its owner, allowing ownership-based permissions to determine who can modify or manage the listing.

### ❤️ Listing Likes

Users can like vehicle listings they are interested in. Likes are stored as separate relationships between users and listings, preventing the same user from liking the same listing multiple times.

### 🔎 Filtering & Search

Vehicle filtering is implemented with **django-filter**, allowing users to narrow down listings based on relevant attributes instead of manually browsing through every available vehicle.

### 📍 Location Data

Listings support structured location information and can be associated with a specific geographic location. This structure also provides a foundation for future location-based functionality.

### 🆔 UUID Identifiers

Important models use **UUIDs** instead of sequential integer identifiers. This makes publicly exposed identifiers less predictable and is useful when model IDs are included in URLs or client-side requests.

### 📧 Email Inquiry

Users can contact a vehicle seller directly from a listing page. The inquiry is submitted asynchronously using **jQuery AJAX**, while Django handles request processing, validation, CSRF protection, and email delivery through SMTP.

The frontend also manages the request state so users receive immediate feedback while the email is being processed.

### 🛡️ Request & CSRF Protection

AJAX requests use Django's built-in CSRF protection without bypassing the framework's security mechanisms. Submitted data is also validated server-side before being processed.

### 🧩 Django Signals

**Django Signals** are used where model-related events need to trigger additional automatic behavior. This keeps event-driven logic separated from views where appropriate.

### 📝 Django Forms & Model Forms

**Django Forms** and **Model Forms** handle structured input processing and validation. This keeps validation close to the data layer and prevents views from becoming unnecessarily complex.

### 🎛️ Customized Django Admin

The Django Admin has been customized to make users, listings, and related application data easier to manage without requiring direct database access.

### 🖼️ Image Uploads

Vehicle listings support image uploads. Images are processed using **Pillow**, while uploaded media is kept separate from the project's static assets.

### 📱 Responsive Frontend

The frontend uses **Bootstrap 5** to provide responsive pages and listing workflows across different screen sizes.

## ⚙️ Backend

The backend is built around Django ORM and a Model-View-Form architecture.

Core backend technologies and concepts include:

- Django ORM
- Model relationships
- UUID Primary Keys
- Django Authentication
- Django Forms & Model Forms
- Django Signals
- django-filter
- Server-Side Validation
- CSRF Protection
- Image & Media Handling
- SMTP Email Integration
- Customized Django Admin

The project is primarily backend-focused, using Django's native capabilities and ecosystem to implement its core application logic.

## 🧰 Tech Stack

| Category | Technology |
|---|---|
| Language | Python |
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

## 🚀 Getting Started

### Requirements

- Python 3.13+
- Git
- A configured SMTP service

### Installation

```bash
git clone <repository-url>
cd <project-directory>

python -m venv venv
```

Activate the virtual environment:

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

After configuring the required environment variables, apply migrations:

```bash
python manage.py migrate
```

Run the development server:

```bash
python manage.py runserver
```

The application will then be available at:

```text
http://127.0.0.1:8000/
```

## 🧪 Testing & QA

The project is being reviewed for:

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

## 📸 Screenshots

Screenshots of the main pages and important application flows will be added here.

## 📌 Project Status

- Backend: **Complete**
- Frontend: **Complete**
- Core Features: **Complete**
- Production Audit: **In Progress**
- Deployment: **Planned**
- Public Release: **Planned**

## 🎯 Project Goals

This project was developed as a practical Django application to demonstrate experience with a real-world, database-driven web application.

The primary focus is Django, database modeling, authentication, validation, asynchronous requests, email integration, file handling, filtering, and application management through Django Admin.

## 👨‍💻 Author

**Mehrshad**

Built with **Python & Django**.
