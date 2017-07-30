Youtube to mp3 converter
========================

Converts youtube videos to mp3 files and sends an email with download link.
All the blocking tasks are done asynchronous so it is safe to use in production.


Setup:
-----

Run the following commands to install all dependencies::


$ pip install -r requirements.txt
$ sudo apt install --assume-yes ffmpeg
$ sudo apt install --assume-yes rabbitmq-server

Start celery daemon::

$ celery -A baseapp.celery worker --loglevel=info

Run dev server (in production use gunicorn)::

$ python manage.py runserver

NOTE: Make sure rabbitmq service is running with default credentials.
---------------------------------------------------------------------

NOTE 2: Mailing service is using sendgrid with my API key. I have left it for conveniece, but please use our own. You can setup your account at Sendgrid_ .

.. _Sendgrid: https://www.sendgrid.com

Change the API Key in youtube_to_mp3/settings.py


