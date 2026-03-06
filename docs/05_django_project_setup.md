# Django Project Setup

## Concept

Django follows a modular architecture where a project is divided into multiple apps.

Each app handles a specific responsibility.

## Project Structure

smart_attendance/
    manage.py
    smart_attendance/
        settings.py
        urls.py
        asgi.py
        wsgi.py

Apps:

- accounts
- attendance
- recognition
- academics

## Why Use Multiple Apps

It keeps the project organized.

accounts → student and teacher management  
attendance → attendance records  
recognition → machine learning logic  
academics → assignments and marks