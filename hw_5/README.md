# hw_5 Project

This is a Django project named `hw_5` that includes a simple Todo application. The project is structured to facilitate easy development and organization of code.

## Project Structure

```
hw_5
├── hw_5
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── todos
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── views.py
│   ├── urls.py
│   ├── migrations
│   │   └── __init__.py
│   ├── templates
│   │   └── todos
│   │       └── index.html
│   └── static
│       └── todos
│           └── styles.css
├── manage.py
└── README.md
```

## Setup Instructions

1. **Clone the repository**:
   ```
   git clone <repository-url>
   cd hw_5
   ```

2. **Create a virtual environment**:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**:
   ```
   pip install django
   ```

4. **Run migrations**:
   ```
   python manage.py migrate
   ```

5. **Create a superuser** (optional, for accessing the admin panel):
   ```
   python manage.py createsuperuser
   ```

6. **Run the development server**:
   ```
   python manage.py runserver
   ```

## Usage

- Access the application at `http://127.0.0.1:8000/`.
- Use the admin panel at `http://127.0.0.1:8000/admin/` to manage todos.
- The Todo app allows users to create, view, update, and delete their todos.

## Features

- User authentication for managing todos.
- CRUD operations for todos.
- Responsive design using Bootstrap.

## License

This project is licensed under the MIT License.