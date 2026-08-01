# Simple Blog / Notes Publishing Website

A minimal, beginner-friendly Django project demonstrating CRUD operations,
Models, Forms, Templates, Static Files, and SQLite. No authentication is
required to use the site — anyone can create, view, edit, delete, and
search blog posts.

## Tech Stack
- Backend: Python, Django (Function-Based Views)
- Database: SQLite
- Frontend: HTML, CSS, Bootstrap 5

## Folder Structure
```
simple_blog/
├── manage.py
├── requirements.txt
├── db.sqlite3
├── simple_blog/          # Project settings & root URLs
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py / asgi.py
├── blog/                 # The blog app
│   ├── models.py         # BlogPost model
│   ├── forms.py          # BlogPostForm
│   ├── views.py          # Function-based views (home, CRUD, search, about, contact)
│   ├── urls.py           # App-level URL routes
│   ├── admin.py          # Admin panel customization
│   ├── migrations/
│   └── templates/blog/   # All HTML templates (base, home, post_form, etc.)
├── static/css/style.css  # Custom CSS (on top of Bootstrap 5)
└── media/blog_images/    # Uploaded featured images (created automatically)
```

## Setup Instructions

1. **Create and activate a virtual environment** (recommended):
   ```
   python -m venv venv
   source venv/bin/activate      # On Windows: venv\Scripts\activate
   ```

2. **Install dependencies**:
   ```
   pip install -r requirements.txt
   ```

3. **Apply database migrations** (a fresh `db.sqlite3` with no data is
   already included, but you can re-run this any time):
   ```
   python manage.py migrate
   ```

4. **Create an admin user** to access the Django admin panel:
   ```
   python manage.py createsuperuser
   ```

5. **Run the development server**:
   ```
   python manage.py runserver
   ```

6. Open your browser at **http://127.0.0.1:8000/**
   Admin panel: **http://127.0.0.1:8000/admin/**

## Features
- **Home Page** – lists all posts as Bootstrap cards (title, short
  description, published date, "Read More").
- **Create Blog** – form with Title, Category (dropdown), Content
  (required) and Featured Image (optional), with validation errors shown.
- **Blog Details** – full post view with image, category, date, content.
- **Edit Blog** – update any post using the same form.
- **Delete Blog** – confirmation page before deleting.
- **Search** – search posts by title from the navbar search box.
- **About / Contact** – static informational pages.
- **Admin Panel** – `list_display`, `search_fields`, and `list_filter`
  configured for `BlogPost`.

## Notes
- Uploaded images are stored in `media/blog_images/` and served via
  Django's development server (`MEDIA_URL` / `MEDIA_ROOT` in settings.py).
- Bootstrap 5 is loaded via CDN in `templates/blog/base.html`, so no
  npm/node build step is needed.
