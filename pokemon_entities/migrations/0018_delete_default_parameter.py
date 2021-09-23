# Generated by Django 3.1.13 on 2021-09-23 08:42

from django.db import migrations, models
import pokemon_entities.custom_storage


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0017_add_related_name_parameter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='description',
            field=models.TextField(blank=True, verbose_name='о покемоне'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='image',
            field=models.ImageField(blank=True, max_length=200, storage=pokemon_entities.custom_storage.OverwriteStorage(), upload_to='', verbose_name='картинка покемона'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='title_en',
            field=models.CharField(blank=True, max_length=200, verbose_name='имя покемона на англ. яз.'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='title_jp',
            field=models.CharField(blank=True, max_length=200, verbose_name='имя покемона на яп. яз.'),
        ),
    ]
