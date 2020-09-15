# api

### Pipenv
[tutorial](https://medium.com/code-rocket-blog/gerenciando-suas-depend%C3%AAncias-e-ambientes-python-com-pipenv-9e5413513fa6)

### Database

* deletar o schema
```
DROP SCHEMA public CASCADE;
CREATE SCHEMA public;
```

* fazer backup de algum banco de dados
```
docker exec -i db pg_dumpall --username=postgres --clean | gzip > backup.sql.gz
```

* restaurar backup
```
psql -p 5432 -U postgres -h localhost < backup.sql.gz
```

### Manage

* migrate
```
./manage.py makemigrations
./manage.py migrate
```

* createsuperuser
```
./manage.py createsuperuser
```

* dumpdata
```
./manage.py dumpdata configuration --indent 4 > configuration.json
./manage.py dumpdata product.client --indent 4 > clientes.json
```

* loaddata
```
./manage.py loaddata configuration.json
./manage.py loaddata clientes.json
```

## Project setup

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

  * Instalar dependências do projeto
    ```
    pipenv install .
    ```

  * Ativar virtualenv
    ```
    pipenv shell
    ```
