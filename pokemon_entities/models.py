from django.db import models

from .custom_storage import OverwriteStorage


class Pokemon(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(max_length=200,
                              null=True,
                              storage=OverwriteStorage())

    def __str__(self):
        return f'{self.title}'


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    lat = models.FloatField()
    lon = models.FloatField()

    def __str__(self):
        human_readable_repr = (
            f'{self.pokemon.title} находится в точке: '
            f'{self.lat}, {self.lon}'
        )
        return human_readable_repr
