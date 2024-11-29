#!/bin/sh

python manage.py makemigrations
python manage.py migrate --no-input
python manage.py collectstatic --no-input

# gunicorn --reload backend.wsgi:application --bind 0.0.0.0:8000 
# gunicorn backend.wsgi:application -w 2 -b :8000 --reload
set -e

# Function to start Gunicorn with dynamic reload-extra-file options
start_gunicorn() {
    # Start Gunicorn
    echo "Starting Gunicorn..."
    gunicorn --config gunicorn-cfg.py --reload --reload-engine=poll backend.asgi:application -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000 
}

# Start Gunicorn
start_gunicorn