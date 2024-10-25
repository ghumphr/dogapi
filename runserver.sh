#!/bin/sh

APP_HOME=/app/webservices
cd $APP_HOME

# We need to run the migrations somewhere, why not when the webserver starts?
python manage.py migrate

# This will simply fail if the admin user already exists
python manage.py createsuperuser --no-input

# Now run the web app...
python manage.py runserver 0.0.0.0:8000

