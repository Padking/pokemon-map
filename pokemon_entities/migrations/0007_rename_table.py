# Generated by Django 3.1.13 on 2021-09-12 06:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0006_delete_previous_version_of_table'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PokemonPEntity',
            new_name='PokemonEntity',
        ),
    ]
