from django.conf import settings
from django.db.models import F, Value as V
from django.db.models.functions import Concat
from django.http import HttpResponseNotFound
from django.shortcuts import render

import folium

from .models import Pokemon, PokemonEntity


MOSCOW_CENTER = [55.751244, 37.618423]
DEFAULT_IMAGE_URL = (
    'https://vignette.wikia.nocookie.net/pokemon/images/6/6e/%21.png/revision'
    '/latest/fixed-aspect-ratio-down/width/240/height/240?cb=20130525215832'
    '&fill=transparent'
)


def add_pokemon(folium_map, lat, lon, image_url=DEFAULT_IMAGE_URL):
    icon = folium.features.CustomIcon(
        image_url,
        icon_size=(50, 50),
    )
    folium.Marker(
        [lat, lon],
        icon=icon,
    ).add_to(folium_map)


def get_pokemons_kind(by_id) -> Pokemon:
    """Возвращает вид покемона при наличии особей."""
    try:
        pokemons_kind = (Pokemon.objects
                         .filter(id__in=PokemonEntity.objects.values('pokemon'))
                         .get(id=by_id))
    except Pokemon.DoesNotExist:
        invalid_id_msg = (
            'Покемон не найден!<br>'
            'Проверьте правильность записи в URL<br>'
            f"идентификатора разновидности покемона '{by_id}'"
        )
        return invalid_id_msg

    return pokemons_kind


def show_all_pokemons(request):

    absolute_uri = f'{request.build_absolute_uri(settings.MEDIA_URL)}'
    pokemons_entities = (PokemonEntity.objects
                         .select_related('pokemon')
                         .values('lat', 'lon', 'pokemon__image')
                         .annotate(img_url=Concat(V(f'{absolute_uri}'),
                                   'pokemon__image')))

    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for pokemon_entity in pokemons_entities:
        add_pokemon(folium_map, pokemon_entity['lat'],
                    pokemon_entity['lon'], pokemon_entity['img_url'])

    pokemons_on_page = (Pokemon.objects
                        .filter(id__in=PokemonEntity.objects.values('pokemon'))
                        .annotate(pokemon_id=F('id'),
                                  title_ru=F('title'),
                                  img_url=Concat(V(f'{absolute_uri}'),
                                  'image')))

    return render(request, 'mainpage.html', context={
        'map': folium_map._repr_html_(),
        'pokemons': pokemons_on_page,
    })


def show_pokemon(request, pokemon_id):

    pokemons_kind = get_pokemons_kind(pokemon_id)
    if isinstance(pokemons_kind, str):
        return HttpResponseNotFound(f'<h1>{pokemons_kind}</h1>')

    pokemon = {}
    absolute_uri = f'{request.build_absolute_uri(settings.MEDIA_URL)}'

    about_pokemon_kind = {
        'title_ru': pokemons_kind.title,
        'title_en': pokemons_kind.title_en,
        'title_jp': pokemons_kind.title_jp,
        'description': pokemons_kind.description,
        'img_url': f'{absolute_uri}{pokemons_kind.image}'
    }
    pokemon.update(about_pokemon_kind)

    previous_evolution_of_pokemon = pokemons_kind.previous_evolution
    if previous_evolution_of_pokemon:
        about_pokemons_ancestor = {
            'previous_evolution': {
                'pokemon_id': previous_evolution_of_pokemon.id,
                'title_ru': previous_evolution_of_pokemon.title,
                'img_url': f'{absolute_uri}{previous_evolution_of_pokemon.image}'
            }
        }
        pokemon.update(about_pokemons_ancestor)

    try:
        next_evolution_of_pokemon = (pokemons_kind.next_evolutions
                                     .annotate(pokemon_id=F('id'),
                                               title_ru=F('title'),
                                               img_url=Concat(V(f'{absolute_uri}'),
                                               'image'))
                                     .values('pokemon_id',
                                             'title_ru',
                                             'img_url')
                                     .get())
    except Pokemon.DoesNotExist:  # Нет потомка у покемона
        pass
    else:
        about_pokemons_descendant = {
            'next_evolution': {
                'pokemon_id': next_evolution_of_pokemon['pokemon_id'],
                'title_ru': next_evolution_of_pokemon['title_ru'],
                'img_url': next_evolution_of_pokemon['img_url']
            }
        }
        pokemon.update(about_pokemons_descendant)

    pokemons_entities = (pokemons_kind.pokemon_pokemonentities.all()
                         .select_related('pokemon')
                         .annotate(img_url=Concat(V(f'{absolute_uri}'),
                                   'pokemon__image'))
                         .values('img_url', 'lat', 'lon'))

    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for pokemon_entity in pokemons_entities:
        add_pokemon(folium_map, pokemon_entity['lat'],
                    pokemon_entity['lon'], pokemon_entity['img_url'])

    return render(request, 'pokemon.html', context={
        'map': folium_map._repr_html_(),
        'pokemon': pokemon
    })
