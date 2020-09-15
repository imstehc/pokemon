from django.forms import CheckboxSelectMultiple
from django_filters import filterset
from core.models import Pokemon, PokemonType

FILTER_LIKE = 'icontains'


# class to filter pokemon by name or types
class PokemonFilter(filterset.FilterSet):
    name = filterset.CharFilter(lookup_expr=FILTER_LIKE)
    types = filterset.ModelMultipleChoiceFilter(
        queryset=PokemonType.objects.all(),
        field_name='types__name',
        to_field_name='name',
        widget=CheckboxSelectMultiple(),
        label='PokemonType',
        label_suffix='',
    )

    class Meta:
        model = Pokemon
        fields = ['name', 'types']
