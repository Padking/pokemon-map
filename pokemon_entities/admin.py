from django.contrib import admin

from .models import Pokemon, PokemonEntity


models_for_admin_interface = (Pokemon, PokemonEntity, )
admin.site.register(models_for_admin_interface)
