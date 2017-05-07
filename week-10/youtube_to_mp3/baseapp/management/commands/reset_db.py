import os
from youtube_to_mp3.settings import MP3_OUTPUT_PATH, DOWNLOAD_VIDEO_PATH
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'Resets db and removes downloaded files'

#    def add_arguments(self, parser):
#       parser.add_argument('book_id', nargs='+', type=int)
#       parser.add_argument('author' , nargs='+', type=str)

    def handle(self, *args, **options):
#       bookid = options['book_id']
#       author = options['author']
        os.remove('db.sqlite3')
        os.system('python manage.py migrate')

        # Remove downloaded files
        for f in os.listdir(MP3_OUTPUT_PATH):
            os.remove(os.path.join(MP3_OUTPUT_PATH,f))

        for f in os.listdir(DOWNLOAD_VIDEO_PATH):
            os.remove(os.path.join(DOWNLOAD_VIDEO_PATH, f))

