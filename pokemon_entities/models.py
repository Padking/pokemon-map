from django.db import models

from .custom_storage import OverwriteStorage


class Pokemon(models.Model):
    title = models.CharField('имя покемона', max_length=200)
    title_en = models.CharField('имя покемона на англ. яз.',
                                blank=True,
                                max_length=200, null=True)
    title_jp = models.CharField('имя покемона на яп. яз.',
                                blank=True,
                                max_length=200, null=True)
    description = models.TextField('о покемоне', blank=True, null=True)
    image = models.ImageField('картинка покемона', blank=True, max_length=200,
                              null=True, storage=OverwriteStorage())
    previous_evolution = models.ForeignKey('self', null=True, blank=True,
                                           on_delete=models.SET_NULL,
                                           related_name='next_evolutions',
                                           verbose_name=(
                                               'из кого эволюционировал'
                                           ))

    def __str__(self):
        return f'{self.title}'


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE,
                                verbose_name='разновидность покемона')
    lat = models.FloatField('широта')
    lon = models.FloatField('долгота')
    appeared_at = models.DateTimeField('время появления',
                                       blank=True, null=True)
    disappeared_at = models.DateTimeField('время исчезновения',
                                          blank=True, null=True)
    level = models.IntegerField('уровень', blank=True, null=True)
    health = models.IntegerField('здоровье', blank=True, null=True)
    strength = models.IntegerField('атака', blank=True, null=True)
    defence = models.IntegerField('защита', blank=True, null=True)
    stamina = models.IntegerField('выносливость', blank=True, null=True)

    def __str__(self):
        human_readable_repr = (
            f'{self.pokemon.title} находится в точке: '
            f'{self.lat}, {self.lon}'
        )
        return human_readable_repr
