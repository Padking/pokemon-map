import os

from django.conf import settings
from django.core.files.storage import FileSystemStorage


class OverwriteStorage(FileSystemStorage):
    """Переопределяет поведение `FileSystemStorage`."""

    def get_available_name(self, name, max_length=None):
        """Удаляет, различающиеся наименованием, картинки."""
        if self.exists(name):
            os.remove(os.path.join(settings.MEDIA_ROOT, name))
        return name
