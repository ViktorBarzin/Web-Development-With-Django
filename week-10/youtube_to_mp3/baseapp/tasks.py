from .models import AudioFile
import uuid
from celery import shared_task

@shared_task
def create_mp3_object_and_return_obj_id(file_path):
        audio_file = AudioFile.objects.create(id=uuid.uuid4(), file_path=file_path)
        return audio_file.id
