from django.apps import AppConfig


class CoreConfig(AppConfig):
    name = 'core'
    verbose_name = "Pokémon"

    # method only used in dev to import the initial data from  pokemon.json at postgres.
    # def ready(self):
    #     import core.connection
