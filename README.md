# Django REST Framework CRUD API

A simple RESTful API built with Django REST Framework that performs CRUD operations on items with PostgreSQL database.

## Project Overview

This project implements a basic CRUD API for managing items with the following functionality:
- Create, Read, Update, and Delete items
- Each item has: name, description, and price
- Built using Django REST Framework with PostgreSQL database
- Includes API documentation and admin interface

## Setup and Installation

### Prerequisites
- Python 3.8+
- Docker Desktop (for PostgreSQL)

### 1. Project Setup
```bash
# Create and navigate to project directory
mkdir api_development
cd api_development

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```

### 2. Install Dependencies
Install dependencies:
```bash
pip install -r requirements.txt
```

### 3. Database Setup

Start PostgreSQL:
```bash
docker-compose up -d
```

### 4. Django Configuration
Create `.env` file with the following info:
```env
SECRET_KEY=your-secret-key-here
DEBUG=True
DATABASE_URL=postgresql://postgres:password@localhost:5432/api_skill_test_django
ALLOWED_HOSTS=localhost,127.0.0.1
```

**Generate a secure SECRET_KEY:**
```bash
# Generate secret key using Django
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"

# Or use Python
python -c "import secrets; print(secrets.token_urlsafe(50))"
```
Copy the generated key and replace `your-secret-key-here` in the `.env` file.

### 5. Run Django
```bash
# Run migrations
python manage.py makemigrations
python manage.py migrate

# Start server
python manage.py runserver
```

## Testing and Development

### Populate Database with Dummy Data
```bash
# Create 10 sample items (default)
python manage.py seed_data

# Create specific number of items
python manage.py seed_data --count 50

# Create 100 items for testing
python manage.py seed_data --count 100
```

### Management Commands
- `python manage.py seed_data` - Creates sample items for testing
- `python manage.py createsuperuser` - Creates admin user
- `python manage.py runserver` - Starts development server

## 📁 Project Structure

```
api-skill-test-django/
├── core/
│   ├── settings.py          
│   ├── urls.py              
│   └── wsgi.py          
├── items/
│   ├── models.py            
│   ├── apps.py            
│   ├── exceptions.py            
│   ├── serializers.py       
│   ├── views.py             
│   ├── urls.py              
│   └── admin.py             
├── .env                     
├── docker-compose.yml       
├── requirements.txt         
└── manage.py               
```

## 🌐 API Endpoints

Base URL: `http://127.0.0.1:8000`

| Method | Endpoint | Description | Response |
|--------|----------|-------------|----------|
| `GET` | `/api/items/` | Get all items | 200 OK |
| `POST` | `/api/items/` | Create new item | 201 Created |
| `GET` | `/api/items/{id}/` | Get specific item | 200 OK |
| `PUT` | `/api/items/{id}/` | Update item (full) | 200 OK |
| `DELETE` | `/api/items/{id}/` | Delete item | 204 No Content |

### Item Data Structure
```json
{
    "id": 1,
    "name": "Item Name",
    "description": "Item description",
    "price": "99.99",
    "created_at": "2025-07-29T10:30:00Z",
    "updated_at": "2025-07-29T10:30:00Z"
}
```

### Example Requests

**Create Item:**
```bash
POST /api/items/
{
    "name": "MacBook Pro",
    "description": "Apple laptop",
    "price": 1999.99
}
```

**Update Item:**
```bash
PUT /api/items/1/
{
    "name": "MacBook Pro 16-inch",
    "description": "Updated description",
    "price": 2299.99
}
```