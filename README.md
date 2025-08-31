# Django Tweet App

A simple tweet application built with Django. Users can register, log in, create, edit, and delete their own tweets. Only the tweet owner can edit or delete their tweets.

## Features

- User registration and authentication
- Create, edit, and delete tweets (with optional photo upload)
- Only tweet owners can edit or delete their tweets
- Responsive Bootstrap UI

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
# On Windows:
.venv\Scripts\activate
# On Mac/Linux:
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply migrations

```bash
python manage.py migrate
```

### 5. Create a superuser (admin)

```bash
python manage.py createsuperuser
```

### 6. Run the development server

```bash
python manage.py runserver
```
visit on /tweet after the ip server

