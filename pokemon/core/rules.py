from core import exceptions


# verify if the team has six pokemon
def team_length(pokemon_validated_data):
    if len(pokemon_validated_data) != 6:
        raise exceptions.TeamLengthNotAllowedException()


# verify if the team name has 5 or more characters
def team_name_length(team_name_validated_data):
    if len(team_name_validated_data) < 5:
        raise exceptions.TeamLengthNameNotAllowedException()

