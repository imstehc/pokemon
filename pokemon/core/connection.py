# class only used in dev to import the initial data from  pokemon.json at postgres.
import json

from django.db.backends.signals import connection_created
from django.dispatch import receiver

from core.choices import POKEMON_TYPE_OPTIONS
from core.models import Pokemon, PokemonType


@receiver(connection_created)
def create_pokemon_db(connection, **kwargs):

    if not Pokemon.objects.all().exists():
        # Read file pokemon.json to data in table created at postgres database
        create_pokemon_types()
        f = open('infra/mongo-seed/pokemon.json')
        json_string = f.read()
        f.close()

        data = json.loads(json_string)

        for pokemon in data:
            items = []
            # create Pokemon model instances
            model_pokemon = Pokemon(id=pokemon.get('id'), name=pokemon.get('name'), height=pokemon.get('height'),
                                    weight=pokemon.get('weight'), image=pokemon.get('image'), xp=pokemon.get('xp'))
            items.append(model_pokemon)

            # create data at pokemon table
            result = Pokemon.objects.bulk_create(items)
            types = PokemonType.objects.filter(name__in=pokemon.get('types'))

            # create data at types table
            for ty in types:
                result[0].types.add(ty)


# method only used in dev to import the initial data from  pokemon.json at database postgres.
def create_pokemon_types():
    # create initial data at pokemon_type table
    if not PokemonType.objects.all().exists():
        for type in POKEMON_TYPE_OPTIONS:
            PokemonType(name=type[1], is_active=True).save()
