# 💃 Multi-Branch Dance Academy Management System

[![Python Version](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Django Version](https://img.shields.io/badge/Django-5.x%20%2F%206.x-green.svg)](https://www.djangoproject.com/)
[![License](https://img.shields.io/badge/License-MIT-amber.svg)](LICENSE)
[![Design](https://img.shields.io/badge/Design-Cultural%20Fusion%20Editorial-maroon.svg)](#-design-system--visual-identity)
[![Deployment](https://img.shields.io/badge/Deploy-Render%20Ready-purple.svg)](#-production--deployment-render)

A modern, full-stack **Dance Academy & School Management Web Application** engineered with Python and Django. Designed specifically for multi-branch dance academies, the platform combines robust academic management with an elegant **"Cultural Fusion"** editorial aesthetic—harmonizing classical heritage arts with modern SaaS efficiency.

---

## 📖 Table of Contents
- [✨ Key Features](#-key-features)
- [🎭 User Roles & Access Control](#-user-roles--access-control)
- [🎨 Design System & Visual Identity](#-design-system--visual-identity)
- [🛠️ Tech Stack & Dependencies](#️-tech-stack--dependencies)
- [📁 Project Architecture](#-project-architecture)
- [🚀 Getting Started](#-getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation & Setup](#installation--setup)
  - [Environment Variables](#environment-variables)
  - [Creating a Superuser](#creating-a-superuser)
  - [Running the Development Server](#running-the-development-server)
- [🌐 URL Routes & Navigation](#-url-routes--navigation)
- [🚢 Production & Deployment (Render)](#-production--deployment-render)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)

---

## ✨ Key Features

- **🏛️ Multi-Branch Management:**
  - Create and manage branch locations across different cities.
  - Assign branch managers and maintain active branch statuses.
  - Filter and oversee batches, students, and courses by branch.

- **🩰 Comprehensive Dance Course Catalog:**
  - Supports classical & modern styles: *Bharatanatyam, Kathak, Odissi, Kuchipudi, Manipuri, Mohiniyattam, Folk Dance, Contemporary, Hip Hop, and Bollywood*.
  - Multi-tier proficiency levels: *Beginner, Intermediate, Advanced, Professional*.
  - Full syllabus details, course durations, and pricing structures.

- **📅 Dynamic Batch Scheduling & Capacity Tracking:**
  - Configure class timings, specific days of the week, and student intake caps.
  - Real-time seating availability calculations with dynamic capacity counters.
  - Direct assignment of qualified faculty instructors to batches.

- **📝 Student Admission & Enrollment Pipeline:**
  - Public & student-facing online admission application flow.
  - Admin/Manager workflow for reviewing, approving, or rejecting admissions.
  - Fee payment tracking (*Unpaid, Partial, Paid*) and ledger notes.

- **📊 Role-Based Dashboards:**
  - Custom views tailored for Super Admins, Admins, Branch Managers, Faculty, and Students.
  - Interactive KPI summary cards (Total Branches, Enrolled Students, Active Batches, Admissions).
  - Quick action shortcuts for daily administrative tasks.

---

## 🎭 User Roles & Access Control

The application implements a custom user model (`accounts.User`) with dedicated permission levels:

| Role | Access Scope & Capabilities |
| :--- | :--- |
| **Super Admin / Admin** | Complete system authority. Manage all branches, courses, batches, admissions, and user accounts. Full access to administrative metrics and Django Admin. |
| **Branch Manager** | Oversees operations for assigned branch locations. Manages branch batches, reviews pending student admissions, and monitors branch enrollments. |
| **Faculty** | Views assigned course batches, class schedules, and enrolled student rosters. |
| **Student** | Browses course offerings and branches, applies for batches, tracks admission status, and monitors enrolled classes. |

---

## 🎨 Design System & Visual Identity

The UI is inspired by a **"Cultural Fusion"** editorial concept—honoring the depth of classical dance forms while delivering clean usability:

- **Color Palette:**
  - **Primary:** Deep Maroon / Burgundy (`#800000`)
  - **Secondary / Accent:** Warm Gold / Muted Saffron (`#D4AF37` / `#F4C430`)
  - **Background:** Warm Ivory / Soft Cream (`#FCF9F2`)
  - **Text & Contrast:** Charcoal / Deep Espresso (`#332211`)
- **Typography:**
  - **Headings:** High-contrast Editorial Serif (*Playfair Display*) for grace and authority.
  - **Body / Interface:** Crisp Modern Sans-Serif (*Poppins / Inter*) for legible metrics and data tables.
- **Components:** Glassmorphic metric cards, delicate gold borders, responsive tables, and mobile-friendly navigation.

---

## 🛠️ Tech Stack & Dependencies

- **Backend Framework:** Django (Python 3.10+)
- **Database:** SQLite (default for development), PostgreSQL (production-ready via `dj-database-url` & `psycopg2-binary`)
- **Static File Handling:** WhiteNoise
- **WSGI / Production Server:** Gunicorn
- **Image & Media Processing:** Pillow
- **Frontend / Styling:** Vanilla CSS + HTML5 templates with responsive CSS Grid & Flexbox

---

## 📁 Project Architecture

```plaintext
├── accounts/          # User authentication, custom User model, registration & role dashboards
├── admissions/        # Student enrollment applications, approval/rejection lifecycle & payments
├── batches/           # Batch scheduling, timetable timings, capacity limits & faculty assignment
├── branches/          # Physical academy branch locations and branch manager mapping
├── config/            # Django project root settings, wsgi/asgi entry points, root URLs
├── courses/           # Dance styles, course descriptions, fee structure, and syllabi
├── static/            # Static assets (custom CSS stylesheets, JavaScript, icons)
├── templates/         # Django HTML templates (base layout, dashboard, auth, app views)
│   ├── accounts/
│   ├── admissions/
│   ├── batches/
│   ├── branches/
│   ├── courses/
│   ├── includes/
│   ├── base.html
│   ├── dashboard.html
│   └── home.html
├── build.sh           # Shell build script for cloud platform deployments (Render)
├── db.sqlite3         # Development database
├── manage.py          # Django CLI utility
└── requirements.txt   # Python package dependencies
```

---

## 🚀 Getting Started

### Prerequisites
- **Python 3.10+** installed on your system ([python.org](https://www.python.org/downloads/))
- **Git** installed on your system ([git-scm.com](https://git-scm.com/))
- `virtualenv` or built-in `venv` module

### Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Devansh1623/Python-Django-Internship-Project.git
   cd Python-Django-Internship-Project
   ```

2. **Create and activate a virtual environment:**
   - **On Windows (PowerShell):**
     ```powershell
     python -m venv venv
     .\venv\Scripts\Activate.ps1
     ```
   - **On macOS / Linux:**
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply database migrations:**
   ```bash
   python manage.py migrate
   ```

### Environment Variables

You can configure optional environment variables in your environment or a `.env` file:

| Variable | Description | Default |
| :--- | :--- | :--- |
| `SECRET_KEY` | Django secret key for cryptographic signing | Insecure dev fallback |
| `DEBUG` | Enable/disable debug mode (`True`/`False`) | `True` (auto-disabled if `RENDER` is set) |
| `DATABASE_URL` | PostgreSQL connection URI | `sqlite:///db.sqlite3` |
| `RENDER_EXTERNAL_HOSTNAME` | Hostname configured on Render deployment | `*` |

### Creating a Superuser

To access the Django Admin and all administrative features:
```bash
python manage.py createsuperuser
```
Follow the prompts to enter a username, email, and password.

### Running the Development Server

Start the local server:
```bash
python manage.py runserver
```

Open your browser and navigate to:
```text
http://127.0.0.1:8000/
```

---

## 🌐 URL Routes & Navigation

| Route Pattern | View Name | Description |
| :--- | :--- | :--- |
| `/` | `home` | Academy landing page with branches and featured courses |
| `/login/` | `login` | User authentication & sign-in |
| `/register/` | `register` | Student registration portal |
| `/logout/` | `logout` | Session sign-out |
| `/dashboard/` | `dashboard` | Dynamic role-based user dashboard |
| `/profile/` | `profile` | User profile page |
| `/branches/` | `branch_list` | Branch management & directory |
| `/branches/create/` | `branch_create` | Add a new branch |
| `/courses/` | `course_list` | Dance styles & course catalog |
| `/courses/create/` | `course_create` | Add a new course offering |
| `/batches/` | `batch_list` | Batch schedules & enrollment caps |
| `/batches/create/` | `batch_create` | Schedule a new batch |
| `/admissions/` | `admission_list` | Admission inquiries & applications |
| `/admissions/apply/` | `admission_apply` | Apply for enrollment |
| `/admin/` | `admin:index` | Django administrative interface |

---

## 🚢 Production & Deployment (Render)

This repository is pre-configured for automated deployment to **[Render](https://render.com/)**:

1. **Build Command:**
   ```bash
   ./build.sh
   ```
   *(Executes `pip install -r requirements.txt`, `collectstatic`, and `migrate`)*

2. **Start Command:**
   ```bash
   gunicorn config.wsgi:application
   ```

3. **Database:** Attach a managed PostgreSQL database and set `DATABASE_URL` in your environment variables.

---

## 🤝 Contributing

Contributions, feature requests, and bug reports are welcome!
1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License.
