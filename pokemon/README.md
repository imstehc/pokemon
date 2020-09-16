# Api Pokemon

### Pipenv
[tutorial](https://medium.com/code-rocket-blog/gerenciando-suas-depend%C3%AAncias-e-ambientes-python-com-pipenv-9e5413513fa6)

### Banco de dados

* Tenha o postgres na sua máquina
* verifique se o banco postgres existe

### Migrações

* Execute as migrações no banco
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