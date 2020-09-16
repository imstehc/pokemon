from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from core import models, serializers, filters


# viewset of router /api/core/pokemon used to list and filter all the pokemons from table
@authentication_classes((JWTAuthentication,))
@permission_classes((IsAuthenticated,))
class PokemonViewSet(viewsets.ModelViewSet):
    queryset = models.Pokemon.objects.prefetch_related('types').all()
    serializer_class = serializers.PokemonSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_class = filters.PokemonFilter
    ordering = ('-id',)


@authentication_classes((JWTAuthentication,))
@permission_classes((IsAuthenticated,))
# viewset of router /api/core/pokemon_team used to store the teams created by the user
# @authentication_classes((JWTAuthentication,))
# @permission_classes((IsAuthenticated,))
class PokemonTeamViewSet(viewsets.ModelViewSet):
    queryset = models.PokemonTeam.objects.all()
    serializer_class = serializers.PokemonTeamSerializer
    ordering_fields = '__all__'
    ordering = ('-id',)