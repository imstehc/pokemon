from rest_framework import serializers
from . import rules
from .models import Pokemon, PokemonTeam, PokemonType


# Class that PokemonType model instance to be converted to native Python datatype that can then be easily
# rendered into JSON
class PokemonTypSerializer(serializers.ModelSerializer):
    class Meta:
        model = PokemonType
        fields = '__all__'


# Class that allow Pokemon model instance to be converted to native Python datatype that can then be easily
# rendered into JSON
class PokemonSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    weight = serializers.CharField()
    height = serializers.CharField()
    xp = serializers.IntegerField()
    types = PokemonTypSerializer(read_only=True, many=True)
    image = serializers.CharField()

    class Meta:
        model = Pokemon
        fields = ['id', 'name', 'weight', 'height', 'xp', 'types', 'image']


# Class that allow Pokemon model instance to be converted to native
# Python datatype that can then be easily rendered into JSON. That class do not have types field because it is not
# necessary to create a team just the pokemon register.
class PokemonWithoutTypesSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    weight = serializers.CharField()
    height = serializers.CharField()
    image = serializers.CharField()
    xp = serializers.IntegerField()

    class Meta:
        model = Pokemon
        fields = ['id', 'name', 'weight', 'height', 'xp', 'image']


# Class that allow PokemonTeam model instance to be converted to native
# Python datatype that can then be easily rendered into JSON.
class PokemonTeamSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    pokemon = PokemonWithoutTypesSerializer(many=True)

    class Meta:
        model = PokemonTeam
        fields = ['name', 'pokemon']

    # method to created the teams. It's was necessary to subscribed that pattern method of django because of the
    # many to many relationship between pokemon table and pokem_types table.
    def create(self, validated_data):
        try:
            # get the fields from data send by user
            pokemon_validated_data = validated_data.pop('pokemon')
            team_name_validated_data = validated_data.__getitem__('name')

            # validate data sended by user
            rules.team_length(pokemon_validated_data)
            rules.team_name_length(team_name_validated_data)

            # create data at pokemon_team and pokemon_pokemon_teams table
            pokemon_team = PokemonTeam.create(pokemon_validated_data, validated_data)
            return pokemon_team

        except Exception as e:
            raise e

