from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView)
from core import viewsets
from django.conf.urls import url


routers = DefaultRouter()

# router to access list of all pokemons
routers.register('pokemon', viewsets.PokemonViewSet, basename='pokemon')

# router to create the pokemon team
routers.register('pokemon_team', viewsets.PokemonTeamViewSet, basename='team')

# urls to authentication
urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    url(r'^token/refresh/$', TokenRefreshView.as_view(), name='token_refresh'),
    url(r'^token/verify/$', TokenVerifyView.as_view(), name='token_verify'),
]

urlpatterns += routers.urls
