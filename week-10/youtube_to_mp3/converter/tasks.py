import os
from celery import shared_task

@shared_task
def convert_to_mp3(input_file):
    # Outputs file with same path but replaces all 'mp4' with 'mp3' along the
    # path. Careful for paths containing mp3. May cause trouble!
    output_file = input_file.replace('mp4', 'mp3')
    convert_cmd = 'ffmpeg -i "{}" "{}"'.format(input_file, output_file)
    os.system(convert_cmd)
    return output_file
