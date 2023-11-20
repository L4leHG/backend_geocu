#!/bin/bash
pip install -r /usr/src/app/requirements.txt

# Collect static files
echo "Collect static files"
python /usr/src/app/manage.py collectstatic --noinput

# Apply database migrations
echo "Apply database migrations"
python /usr/src/app/manage.py makemigrations
python /usr/src/app/manage.py migrate

# Start server
echo "Starting server"
python /usr/src/app/manage.py runserver 0.0.0.0:8000




