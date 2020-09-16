# Api Pokemon

### Ambiente Pipenv
Para controle dos pacotes foi utilizado o pipenv.
[tutorial](https://medium.com/code-rocket-blog/gerenciando-suas-depend%C3%AAncias-e-ambientes-python-com-pipenv-9e5413513fa6)

### Banco de dados
1. Configuração
* Para executar a aplicação é necessário ter o Postgres configurado na máquina, pode ser via instalador do programa no computador ou por meio do docker-compose.yml que está no diretório infra.
* Se já possui o docker instalado na máquina, vá até o diretório anterior infra e execute o comando abaixo em um terminal:
```
 docker-compose up -d db
```
* verifique se o banco postgres existe.

2. Tabelas
* De acordo com o arquivo disponibilizado para a solução (pokemon.json) o banco de dados foi desenvolvido contendo as seguintes tabelas:
1. pokemon - tabela que armazena os dados importados do arquivo disponibilizado pokemon.json.
2. pokemon_type - tabela que armazena os tipos de pokemons mapeados no arquivo pokemon.json.
3. pokemon_types - tabela de relacionamento entre pokemon e pokemon_type, gerada pelo django.
4. pokemon_team - tabela para armazenar os cadastros dos times pelo usuário.
5. pokemon_team_pokemon - tabela de relacionamento entre pokemon_team e pokemon, gerada também pelo django.
6. core_customuser - tabela que armazena o cadastro do usuário, essa tabela é uma extensão da tabela padrão do django.


### Migrações

* Execute as migrações no banco para criar as tabelas utilizadas na solução.
```
 python manage.py migrate
```

* Execute o loaddata inicial para adicionar o usuário default e os dados na tabela
pokemon
```
python manage.py  loaddata core/fixtures/default_user.json
python manage.py  loaddata core/fixtures/pokemon_fixture.json
```

## Configuração do Projeto

### Dependências

* Pyenv - Gerenciador de versão do Python - https://github.com/pyenv/pyenv
* Python 3.7.x
* Pipenv - Gerenciador de pacotes Python - https://docs.pipenv.org

### Criar uma virtualenv
 * Instale a versão python
    ```
    pyenv install 3.7.4
    ```

  * Defina na pasta raiz do projeto a versão python
    ```
    pyenv local 3.7.4
    ```

  * Instale o pipenv na versão python selecionada
    ```
    pip install pipenv
    ```

  * Ativar virtualenv
    ```
    pipenv shell
    ```
   
    * Instalar dependências do projeto
    ```
    pipenv install 
    pip install -r requirements.txt
    ```
