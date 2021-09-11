from django.db import models

from .custom_storage import OverwriteStorage


class Pokemon(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(max_length=200,
                              null=True,
                              storage=OverwriteStorage())

    def __str__(self):
        return f'{self.title}'
