# 📝 Django Blog Application

A simple blog platform built with Django. It supports user registration, login via email, post creation/editing/deletion, and author dashboards.

---

## 🚀 Features

- User registration (as author)
- Email-based login
- Create, edit, and delete blog posts
- View posts by author
- Post status display (draft/published)
- Author dashboard
- Access control: only authors can edit/delete their posts

---

## 🔧 Tech Stack

- Python 3.12+
- Django 5.2.4
- SQLite3 (default)
- Bootstrap (for styling, optional)

---

## 📁 Project Structure

```
Blog/
├── blogapp/
│   ├── migrations/
│   ├── templates/
│   │   └── blogapp/
│   │       ├── home.html
│   │       ├── login.html
│   │       ├── register_author.html
│   │       ├── post_detail.html
│   │       ├── create_post.html
│   │       ├── edit_post.html
│   │       ├── confirm_delete.html
│   │       └── author_dashboard.html
│   ├── static/
│   ├── __init__.py
│   ├── views.py
│   ├── models.py
│   ├── forms.py
│   └── urls.py
├── Blog/
│   ├── __init__.py
│   ├── urls.py
│   └── settings.py
└── manage.py
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/yourusername/django-blog.git
cd django-blog
```

### 2. Create a Virtual Environment

```bash
python3 -m venv env
source env/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

> If you don’t have a `requirements.txt`, run:  
> `pip freeze > requirements.txt` to generate one.

### 4. Run Migrations

```bash
python manage.py migrate
```

### 5. Create a Superuser (for admin panel)

```bash
python manage.py createsuperuser
```

### 6. Run the Server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/blog/` to see the app.

---

## 🧪 Sample URLs

| Page              | URL                                |
|-------------------|-------------------------------------|
| Home              | `/blog/`                            |
| Register Author   | `/blog/register/`                   |
| Login             | `/blog/login/`                      |
| Create Post       | `/blog/create/`                     |
| Post Detail       | `/blog/post/<slug>/`                |
| Edit Post         | `/blog/post/<slug>/edit/`           |
| Delete Post       | `/blog/post/<slug>/delete/`         |
| Author Dashboard  | `/blog/dashboard/<username>/`       |

---

## 🔐 Auth Notes

- Users are registered using **email, username, and password**.
- Login is handled using **email lookup → username auth**.
- Authors can **only edit or delete their own posts**.
- CSRF protection and message feedback are enabled in forms.

---

## 🙌 Credits

Built with ❤️ using Django by DENES MBEZI.

---

## 📜 License

MIT License. See `LICENSE` file for details.
