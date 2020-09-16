## Projeto setup
Para configuração local do projeto em alguma ferramenta de desenvolvimento como o pycharm siga os passos descritos abaixo.

### Pipenv
[tutorial](https://medium.com/code-rocket-blog/gerenciando-suas-depend%C3%AAncias-e-ambientes-python-com-pipenv-9e5413513fa6)

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
    ```
    
   * Instalar a dependência djangorestframework-simplejwt  
    ```
    pip install -r requirements.txt
    ```
