Youtube to mp3 converter

Converts youtube videos to mp3 files and sends an email with download link.
All the blocking tasks are done asynchronous so it is safe to use in production.


Setup:

pip install -r requirements.txt
sudo apt install --assume-yes ffmpeg
sudo apt install --assume-yes rabbitmq-server

Start celery daemon

celery -A baseapp.celery worker --loglevel=info

Run dev server (in production use gunicorn)
python manage.py runserver

NOTE: Make sure rabbitmq service is running with default credentials.



