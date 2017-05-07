import os
import re
import uuid
from django.db import models
from django.dispatch import receiver

# Create your models here.
from youtube_to_mp3.settings import MEDIA_ROOT


class AudioFile(models.Model):
    file_path = models.FileField(upload_to=os.path.join(MEDIA_ROOT, 'mp3'))
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def delete(self):
        if self.file_path:
            os.remove(str(self.file_path))

    # Redefining __str__ in order to save files on the file system with uuids and
    # when a user downloads them, downloads the file without the uuid part
    def __str__(self):
        uuid_pattern = '[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}'
        result = re.sub(uuid_pattern, '', os.path.basename(str(self.file_path)))
        return result


