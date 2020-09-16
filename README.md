
# 1. Descrição da solução

O objetivo desse projeto é permitir que as pessoas jogadoras do jogo Pokémon possam montar seus times baseado em algumas informações básicas sobre os personagens do jogo. Para facilitar e acelerar o desenvolvimento da solução, foram utilizadas tecnologias que possuem um kit flexível/personalizável para construir apis web e que permitem também que os serviços gerados pela solução sejam disponibilizados de forma mais fácil e rápida.

O projeto está organizado em 3 diretórios: um que compreende os artefatos para build da imagem base  contendo todos os módulos pips utilizados na solução **(base-images)**, uma API RESTFul **(projeto pokemon)** e um diretório contendo os artefatos de configuração do projeto em containers docker **(infra)**.



## 1.1 Tecnologias e ferramentas utilizadas
* Python 3.7 - Foi utilizada por ser uma das linguagens de programação mais acessíveis atualmente, pois possui sintaxe simplificada e não complicada, o que dá mais ênfase à linguagem natural o que simplifica o desenvolvimento das soluções;
* Django Rest Framework - foi utilizado possuir um kit de ferramentas poderoso e flexível para construir APIs para Web, por possuir embutido políticas de autenticação, incluindo pacotes para OAuth1a e OAuth2. A sua Serialização suporta fontes de dados ORM e não ORM, totalmente personalizável, além de possuir uma documentação extensa e grande suporte da comunidade.
* Docker -  Por facilitar a distribuição da solução em outras máquinas de forma rápida e confiável.
* PostgreSQL 12 - O PostgreSQL vem com muitos recursos destinados a ajudar os desenvolvedores a construir aplicativos, administradores para proteger a integridade dos dados e criar ambientes tolerantes a falhas, além de ser gratuito e de código aberto;
* Postman - Por simplificar o processo de teste de uma api rest.



## 1.2 Acessos
O projeto pokemon integra-se com serviços que permitem o usuário listar os pokemons encontrados na base de dados por meio de filtros por nome e tipo, além de permitir o cadastro de times contendo 6 pokémons. Para acessar estes serviços e visando a segurança da solução, as rotas criadas foram 'fechadas' por meio de um token válido.

Dados do usuário default da aplicação utilizados para gerar o token válido
* Usuário: ash
* Senha: pikachu


## 1.3 Configurações
Como uma forma de facilitar o uso da solução em outras máquinas, a versão atual da solução será disponibilizada por meio de imagens Docker. Na próxima seção serão detalhados os procedimentos para instalação de cada um dos softwares necessários para execução da aplicação, e os exemplos apresentados farão referência aos procedimentos que foram utilizados para configuração do ambiente mencionado neste documento.


Instalação dos pré-requisitos

Nesta seção serão detalhados os procedimentos para instalação dos pré-requisitos especificados na seção anterior. Se o seu ambiente já possui algum dos softwares necessários instalados, avance para o item seguinte.
Os pré-requisitos para instalação e configuração do produto são os seguintes:
* Sistema Operacional Linux;
* Docker CE;

Os demais requisitos de software serão instalados pelo Docker, de acordo com cada serviço especificado nos arquivos de scripts que foram criados no arquivo infra/Makefile e no arquivo docker-compose.yml contido no diretório infra.
Observação importante:
Estes softwares não devem ser diretamente instalados na máquina,  pois serão instalados e gerenciados em containers do Docker. A instalação duplicada implicará em conflitos e impedirá o correto funcionamento da aplicação.
As versões especificadas neste documento são as que foram utilizadas durante o desenvolvimento, testes e homologação do produto, e recomenda-se que sejam mantidas para o ambiente de produção.
A seguir serão fornecidas orientações específicas para cada item e os comandos que podem ser utilizados para instalação dos softwares na distribuição linux utilizada pela aplicação em seu ambiente atual (Ubuntu Server 18.04). 

## 1.4 Docker
Para configuração dos serviços é necessário instalar o Docker, uma aplicação que gerencia containers onde serão executados de maneira isolada os serviços da API do sistema.
O seguinte link pode ser utilizado como referência para configuração da aplicação:

* Instalação do Docker no Ubuntu: https://www.linode.com/docs/applications/containers/install-docker-ce-ubuntu-1804

## 1.5 Configuração do projeto
Após a configuração do servidor com os pré-requisitos de software, será necessário iniciar os serviços no Docker.

## 1.5.1 Configuração dos serviços docker
A configuração do projeto compreende duas etapas: baixar as imagens com o Docker e executar os serviços, que estão especificados nos arquivos **.yml**, e então iniciar os containers.
Para facilitar o gerenciamento da comunicação de dados entre containers e os nós externos ao ambiente docker, é utilizado uma rede (network) abstrata. Se o sistema será utilizado pela primeira vez no servidor, será necessário realizar essa configuração antes de iniciar os serviços. Para configurar a network que será utilizada pelos containers acesse a raiz do diretório **infra** e execute o script **create-network-docker** que se encontra no arquivo Makefile com o comando
```
make create-network-docker

```


## 1.5.2 Configuração do backend (pokemon)

O projeto do backend foi feito em Python 3.7 utilizando a versão 3.0.3 do framework Django. O gerenciador de banco de dados utilizado no projeto é o Postgres versão 12. Todos estes serviços são executados em containers do Docker, que são instâncias de imagens linux contendo somente os recursos necessários para executar os serviços. Não é necessário a criação do banco de dados, o mesmo será criado quando o container foi iniciado.
Para iniciar a api execute o script **deploy** que está no arquivo Makefile, dentro do diretório infra. 
```
make deploy

```

O arquivo executado realizará o download das imagens já buildadas da aplicação e que foram armazenados no meu repositório pessoal no registry.gitlab.com. O script realiazará também a configuração de um login inicial **(seção 1.2)**, para que o usuário possa acessar as rotas de listagem dos pokémons e cadastro dos times. Após estes procedimentos a API Restful estará disponível em  http://127.0.0.1:8000.

Obs: para informações sobre como configurar o projeto pokémon localmente em alguma IDE, acesse o readme que está no diretório **pokemon/**.


Para verificar a situação dos serviços executando no docker, utilize o comando abaixo:
>docker ps

# 2. Guia de uso
Obs: nessa seção recomenda-se o uso da ferramenta postman para facilitar o processo de teste da api.

Para utilizar as rotas da api é necessário gerar um token válido usando os dados de acesso que estão na seção 1.2 e passá-lo no header da request. 
A geração desse token pode ser feita de duas formas:
1. executando o comando abaixo em um terminal bash.

```
     curl \
    -X POST \
    -H "Content-Type: application/json" \
    -d '{"username": "ash", "password": "pickachu"}' \
    http://localhost:8000/api/core/token

```

2. Importando o arquivo **pokemon.postman_collection.json** que se encontra no diretório pokemon para aplicação postman e acessando a url 
  ``` http://127.0.0.1:8000/api/core/token``` disponível na coleção importada.
  

## 2.1. Listar pokémons por nome e tipo
Para realizar essa operação, é necessário acessar a coleção **pokemon** importada anteriormente no postman e abrir o método GET ``` http://127.0.0.1:8000/api/core/pokemon/?name=nome_pokemon/?types=tipo_pokemon```

Para filtrar por nome ou tipo basta trocar **nome_pokemon** e **tipo_pokemon** para as strings desejadas na busca.
Para trazer todos os pokémons é necessário remover os parametros de filtro da url.



## 2.2 Cadastrar times 
A criação dos times pode ser feita acessando o método POST ```http://127.0.0.1:8000/api/core/pokemon_team/``` , adicionando no header o Authorization Bearer + token gerado anteriormente e no body as informações para o cadastro como no json de exemplo abaixo:
```
{
    "name": "TEAM 7",
    "pokemon": [{
        "id": 100,
        "name": "voltorb",
        "weight": "10.4",
        "height": "0.5",
        "xp": 112,
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/100.png"
    },
    {
        "id": 101,
        "name": "electrode",
        "weight": "66.6",
        "height": "1.2",
        "xp": 112,
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/101.png"
    }, 
    {
        "id": 125,
        "name": "electabuzz",
        "weight": "30.0",
        "height": "1.1",
        "xp": 112,
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/125.png"
    },
    {
        "id": 135,
        "name": "jolteon",
        "weight": "24.5",
        "height": "0.8",
        "xp": 112,
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/135.png"
    },
    {
        "id": 145,
        "name": "zapdos",
        "weight": "52.6",
        "height": "1.6",
        "xp": 112,
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/145.png"
    },
    {
        "id": 170,
        "name": "chinchou",
        "weight": "12.0",
        "height": "0.5",
        "xp": 112,
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/170.png"
    }],
    "trainer": {
        "id": 2
    }
}
```
## 2.3 Listar times cadastrados
Para visualizar todos os times cadastrados é necessário apenas acessar novamente a coleção **pokemon** que foi importada no postman e abrir o método GET da seguinte url: 
``` http://127.0.0.1:8000/api/core/pokemon_team/```. 

## Informações adicionais
* autor(a): Stephany Silva.
* e-mail: stephanycastro.es@gmail.com

