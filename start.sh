#! /bin/bash

echo "Starting docker django app"
exec gunicorn blog.wsgi:application --bind 0.0.0.0:8000 --workers 3
