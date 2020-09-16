from django.contrib.auth.models import AbstractUser, Group, UserManager
from django.db.models import Model, DateTimeField, BooleanField, CharField, BigAutoField, \
    ManyToManyField, IntegerField, ForeignKey, CASCADE
from .choices import POKEMON_TYPE_OPTIONS


class BaseModel(Model):
    id = BigAutoField(primary_key=True, verbose_name='id')
    created = DateTimeField(verbose_name='cadastrado em', auto_now_add=True, editable=False)
    last_updated = DateTimeField(verbose_name='atualizado em', auto_now=True, editable=False)
    is_active = BooleanField(verbose_name='ativo', default=True, db_index=True)

    class Meta:
        abstract = True


class PokemonType(BaseModel):
    # model used to create and manipulate pokemon_type table data
    class Meta:
        verbose_name = 'Tipo de pokémon'
        verbose_name_plural = 'Tipos de pokémons'
        db_table = 'pokemon_type'

    name = CharField(max_length=255, blank=False, null=False, choices=POKEMON_TYPE_OPTIONS, verbose_name='Nome')

    def __str__(self):
        return self.name


class Pokemon(Model):
    # model used to create and manipulate pokemon table data
    class Meta:
        verbose_name = 'Pokémon'
        verbose_name_plural = 'Pokémons'
        db_table = 'pokemon'

    id = BigAutoField(primary_key=True, verbose_name='id')
    name = CharField(max_length=255, blank=False, null=False, unique=True, verbose_name='Nome')
    height = CharField(max_length=255, blank=False, null=False, unique=False, verbose_name='Altura')
    weight = CharField(max_length=255, blank=False, null=False, unique=False, verbose_name='Largura')
    xp = IntegerField(blank=False, null=False, unique=False, verbose_name='Experiência', default=0)
    types = ManyToManyField(PokemonType, related_name='type_pokemon')
    image = CharField(max_length=455, blank=False, null=False, unique=True, verbose_name='Imagem')

    def __str__(self):
        return self.name


class PokemonTeam(BaseModel):
    # model used to create and manipulate pokemon_team table data
    class Meta:
        verbose_name = 'Time de pokémon'
        verbose_name_plural = 'Times de pokémons'
        db_table = 'pokemon_team'

    name = CharField(max_length=255, blank=False, null=False, unique=True, verbose_name='Nome')
    pokemon = ManyToManyField(Pokemon, related_name='pokemon_pokemon_team')
    trainer = ForeignKey('CustomUser', on_delete=CASCADE, default=0)

    @staticmethod
    def create(pokemon_validated_data, validated_data):
        # get the user to set at pokemon team table
        user = CustomUser.objects.get(pk=validated_data.get('trainer').get('id'))

        new_team = {
            "name": validated_data.get('name'),
            "trainer": user,
        }

        # create data at pokemon_team and pokemon_pokemon_teams table
        pokemon_team = PokemonTeam.objects.create(**new_team)
        for pokemon in pokemon_validated_data:
            pokemon = Pokemon.objects.get(pk=pokemon.get('id'))
            pokemon_team.pokemon.add(pokemon)
        return pokemon_team
    
    def __str__(self):
        return self.name


class CustomUser(AbstractUser):
    # model used to authenticate user before access routers of core

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
