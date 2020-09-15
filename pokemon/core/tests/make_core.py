# file to mock the data to tests
from model_mommy.recipe import Recipe
from core.models import Pokemon, PokemonType, CustomUser


def __pokemon_type_recipe():
    return Recipe(PokemonType)


# mock data at pokemon types table
def make_pokemon_type(id, type):
    mock_data = {
        "id": id,
        "is_active": True,
        "name": type
    }
    return __pokemon_type_recipe().make(**mock_data)


# mock data at pokemon table
def make_pokemon(id, type1, type2, name, image):
    items = []
    model_pokemon = Pokemon(id=id, name=name, height=0.7,
                            weight=6.9, xp=64,
                            image=image,
                            )
    items.append(model_pokemon)
    result = Pokemon.objects.bulk_create(items)
    types = PokemonType.objects.filter(id__in=(type1, type2))

    for ty in types:
        result[0].types.add(ty)
    return result[0]


# mock data at custom user table
def make_user():
    user = CustomUser(id=1, email='ash@gmail.com', first_name='Ash', last_name='Ketchum',
                      username='ash', password='pikachu', is_active=True, is_staff=True, is_superuser=True)
    user.save()
    return user

