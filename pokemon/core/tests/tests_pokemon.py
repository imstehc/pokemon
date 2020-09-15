import json
from core.helpers import BaseAPITestCase
from core.messages import ERROR_LENGTH_TEAM, ERROR_LENGTH_TEAM_NAME, ERROR_TEAM_WITHOUT_NAME
from core.models import Pokemon
from core.tests.make_core import make_pokemon, make_pokemon_type, make_user
from core.tests.test_variables import TOKEN, TEAM_3, TEAM_WITHOUT_NAME, \
    TEAM_NAME_4_CHARACTERS


class UserTestClass(BaseAPITestCase):
    def setUp(self):
        # create pokemon types
        self.pokemon1_type = make_pokemon_type(12, 'grass')
        self.pokemon1_type2 = make_pokemon_type(4, 'poison')

        # pokemon used at tests
        self.expected_name = "bulbasaur"
        self.expected_name2 = "electrode"
        self.expected_type1 = "grass"
        self.expected_type2 = "poison"

        # create register to the pokemon
        self.pokemon1 = make_pokemon(1, self.pokemon1_type.id, self.pokemon1_type2.id, self.expected_name,
                                     'image1')

        # create register to the pokemon 2
        self.pokemon1 = make_pokemon(2, self.pokemon1_type.id, self.pokemon1_type2.id, self.expected_name2,
                                     'image2')

        # create register to the pokemon trainer
        self.user = make_user()

        # token the will be used to access the routers
        self.token = TOKEN
        self.url_pokemon = '/api/core/pokemon/'
        self.url_pokemon_team = '/api/core/pokemon_team/'

    def tearDown(self):
        pass

    # test to verify register of data at pokemon table
    def test_create_pokemon_and_pokemon_type(self):
        expected = "bulbasaur"
        types = Pokemon.objects.prefetch_related('types').all().values('types').exists()
        self.assertTrue(types)
        self.assertEqual(self.expected_type1, self.pokemon1_type.name)

    # test to verify filter of all pokemon's registered
    def test_list_all_pokemon(self):
        data = self.client.get(self.url_pokemon, HTTP_AUTHORIZATION='Bearer ' + self.token)
        self.assertEqual(data.status_code, 200)

        pokemon = data.data[0]
        self.assertEqual(pokemon.get('name'), self.expected_name)
        self.assertEqual(pokemon.get('types')[0].get('name'), self.expected_type1)
        self.assertEqual(pokemon.get('types')[1].get('name'), self.expected_type2)

    # test to verify filter by name
    def test_list_pokemon_by_name(self):
        name = "bulbasaur"
        data = self.client.get(self.url_pokemon + "?name=" + name, HTTP_AUTHORIZATION='Bearer ' + self.token)
        self.assertEqual(data.status_code, 200)

        pokemon = data.data[0]
        self.assertEqual(pokemon.get('name'), self.expected_name)
        self.assertEqual(pokemon.get('types')[0].get('name'), self.expected_type1)
        self.assertEqual(pokemon.get('types')[1].get('name'), self.expected_type2)

    # test to verify filter by name
    def test_list_pokemon_by_name_that_not_exist(self):
        name = "pikachu"
        data = self.client.get(self.url_pokemon + "?name=" + name, HTTP_AUTHORIZATION='Bearer ' + self.token)
        self.assertEqual(data.status_code, 200)

        pokemon = data.data
        self.assertEqual(pokemon, [])

    # test to verify filter by type
    def test_list_pokemon_by_type(self):
        types = "grass"
        data = self.client.get(self.url_pokemon + "?types=" + types, HTTP_AUTHORIZATION='Bearer ' + self.token)
        self.assertEqual(data.status_code, 200)

        pokemon = data.data[0]
        self.assertEqual(pokemon.get('name'), self.expected_name)
        self.assertEqual(pokemon.get('types')[0].get('name'), self.expected_type1)
        self.assertEqual(pokemon.get('types')[1].get('name'), self.expected_type2)

    # test to verify filter by name and one type
    def test_list_pokemon_by_name_and_one_type(self):
        name = "bulbasaur"
        data = self.client.get(self.url_pokemon + "?name=" + name + "&types=" + self.expected_type1,
                               HTTP_AUTHORIZATION='Bearer ' + self.token)
        self.assertEqual(data.status_code, 200)

        pokemon = data.data[0]
        self.assertEqual(pokemon.get('name'), self.expected_name)
        self.assertEqual(pokemon.get('types')[0].get('name'), self.expected_type1)
        self.assertEqual(pokemon.get('types')[1].get('name'), self.expected_type2)

    # test to verify filter by name and two type
    def test_list_pokemon_by_name_and_two_type(self):
        name = "bulbasaur"
        data = self.client.get(self.url_pokemon + "?name=" + name + "&types=" + self.expected_type1 + "&types=" +
                               self.expected_type2, HTTP_AUTHORIZATION='Bearer ' + self.token)
        self.assertEqual(data.status_code, 200)

        pokemon = data.data[0]
        self.assertEqual(pokemon.get('name'), self.expected_name)
        self.assertEqual(pokemon.get('types')[0].get('name'), self.expected_type1)
        self.assertEqual(pokemon.get('types')[1].get('name'), self.expected_type2)

    # test to verify if is not permitted to create a team with less than 6 pokemon
    def teste_save_team_only_two_pokemon(self):

        data = self.client.post(self.url_pokemon_team, content_type='application/json',
                                data=json.dumps(TEAM_3), HTTP_AUTHORIZATION='Bearer ' + self.token)
        self.assertEqual(data.status_code, 500)
        self.assertEqual(data.data.get('detail'), ERROR_LENGTH_TEAM)

    # test to verify if is possible to create a team without name
    def teste_save_team_without_field_name(self):

        data = self.client.post(self.url_pokemon_team, content_type='application/json',
                                data=json.dumps(TEAM_WITHOUT_NAME), HTTP_AUTHORIZATION='Bearer ' + self.token)
        self.assertEqual(data.status_code, 400)
        self.assertEqual(data.data.get('name')[0], ERROR_TEAM_WITHOUT_NAME)

    # test to verify if is possible to create a team name with less than 5 characters
    def teste_save_team_with_name_less_than_5_characters(self):

        data = self.client.post(self.url_pokemon_team, content_type='application/json',
                                data=json.dumps(TEAM_NAME_4_CHARACTERS), HTTP_AUTHORIZATION='Bearer ' + self.token)
        self.assertEqual(data.status_code, 500)
        self.assertEqual(data.data.get('detail'), ERROR_LENGTH_TEAM_NAME)
