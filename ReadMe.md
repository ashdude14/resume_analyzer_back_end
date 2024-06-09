# Resume Analyzer (Back-end)

## Overview

Resume Analyzer(Back-end) is a Django-based RESTful API application. This document outlines the project structure and provides an overview of each component.


## Directory Details

### Root Directory
- **manage.py**: Django's command-line utility for administrative tasks.

### `resume_analyzer/` Directory
- **settings.py**: Central settings file.
- **urls.py**: URL configuration for the project.
- **wsgi.py**: WSGI configuration for deployment.
- **asgi.py**: ASGI configuration for asynchronous support.

### `apps/` Directory
A directory to contain all Django apps. Each app is self-contained and has the following structure:
- **admin.py**: Configuration for the Django admin interface.
- **apps.py**: App-specific configuration.
- **models.py**: Data models for the app.
- **serializers.py**: Serializers for converting data to/from JSON.
- **views.py**: API views for handling requests and returning responses.
- **urls.py**: URL configuration for the app.
- **tests.py**: Unit tests for the app.
- **migrations/**: Database migrations for the app.

### `config/` Directory
- **settings/**: Directory for settings files.
  - **base.py**: Base settings common to all environments.
  - **local.py**: Local development settings.
  - **production.py**: Production settings.
- **urls.py**: Central URL configuration.
- **wsgi.py**: WSGI configuration for deployment.
- **asgi.py**: ASGI configuration for asynchronous support.

### `requirements/` Directory
- **base.txt**: Base dependencies for the project.
- **local.txt**: Additional dependencies for local development.
- **production.txt**: Additional dependencies for production.

### `scripts/` Directory
- Custom management scripts.

### `static/` Directory
- Static files.

### `media/` Directory
- User-uploaded files.

### `docs/` Directory
- Documentation for the project.
  - **api/**: API documentation files.

## Best Practices

1. **Modularize Settings**: Separate settings into `base.py`, `local.py`, and `production.py` to manage different configurations for different environments.
2. **Reusable Apps**: Each app should be self-contained with its own models, views, serializers, and tests.
3. **Use Serializers**: Define serializers in a dedicated `serializers.py` file for each app to handle data conversion and validation.
4. **API Versioning**: Include version numbers in your URLs, e.g., `/api/v1/myapp/`.
5. **Documentation**: Maintain up-to-date documentation for your API in the `docs/` directory. Use tools like Swagger or ReDoc for API documentation.

## Setup Instructions

1. Clone the repository:
    ```sh
    git clone ashdude14/resume_analyzer_back_end.git
    cd resume_analyzer
    ```

2. Create a virtual environment and install dependencies:
    ```sh
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements/base.txt
    pip install -r requirements/local.txt  # For local development
    ```

3. Apply migrations and start the development server:
    ```sh
    python manage.py migrate
    python manage.py runserver
    ```

## Running Tests

Run tests using the Django test framework:
```sh
python manage.py test

