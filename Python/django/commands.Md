
pip install django
pip install djangorestframework

To start with:
django-admin startproject mysite
python manage.py runserver
Check from this URL: localhost:8000

To create app under thr project:
python manage.py startapp myapi
To migrate initial models:
python manage.py migrate

To setup admin user:
python manage.py createsuperuser
python manage.py runserver
localhost:8000/admin

For newly added models:
python manage.py makemigrations
python manage.py migrate

Refer: https://medium.com/swlh/build-your-first-rest-api-with-django-rest-framework-e394e39a482c
