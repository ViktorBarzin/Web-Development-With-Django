from uuid import uuid4
from pytube import YouTube
from celery import shared_task


@shared_task
def download_video(url, file_path):
    # To url validation here or in decorator
    yt = YouTube(url)

    video = yt.get('mp4', '360p')
    yt.set_filename('{}{}'.format(yt.filename, str(uuid4())))
    video.download(file_path)

    return file_path + yt.filename + '.mp4'
