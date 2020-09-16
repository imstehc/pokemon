# 1. Introdução

O objetivo desse projeto é permitir que as pessoas jogadoras do jogo Pokémon possam montar seus times baseado em algumas informações básicas sobre os personagens do jogo. Para facilitar e acelerar o desenvolvimento da solução, foram utilizadas tecnologias que possuem um kit de flexível para construir apis web, que permitem também que os serviços gerados pela solução sejam disponibilizados de forma mais fácil e rápida.

O projeto está organizado em 3 diretórios: um que compreende os artefatos para build da imagem base  contendo todos os módulos pips utilizados na solução **(base-images)**, uma API RESTFul **(projeto pokemon)** e um diretório contendo os artefatos de configuração do projeto em containers docker **(infra)**.



## 1.1 Tecnologias utilizadas
* Python 3.7 - Foi utilizada por ser uma das linguagens de programação mais acessíveis atualmente, pois possui sintaxe simplificada e não complicada, o que dá mais ênfase à linguagem natural o que simplifica o desenvolvimento das soluções;
* Django Rest Framework - foi utilizado possuir um kit de ferramentas poderoso e flexível para construir APIs para Web, por possuir embutido políticas de autenticação, incluindo pacotes para OAuth1a e OAuth2. A sua Serialização suporta fontes de dados ORM e não ORM, totalmente personalizável, além de possuir uma documentação extensa e grande suporte da comunidade.
* Docker -  Por facilitar a distribuição da solução em outras máquinas de forma rápida e confiável.
* PostgreSQL 12 - O PostgreSQL vem com muitos recursos destinados a ajudar os desenvolvedores a construir aplicativos, administradores para proteger a integridade dos dados e criar ambientes tolerantes a falhas, além de ser gratuito e de código aberto;



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
Os seguintes links podem ser utilizados como referência para configuração da aplicação:

* Instalação do Docker no Ubuntu: https://www.linode.com/docs/applications/containers/install-docker-ce-ubuntu-1804

## 1.5 Configuração do projeto
Após a configuração do servidor com os pré-requisitos de software, será necessário iniciar os serviços no Docker.

## 1.5.1 Configuração dos serviços docker
A configuração do projeto compreende duas etapas: baixar as imagens com o Docker e executar os serviços, que estão especificados nos arquivos **.yml**, e então iniciar os containers.
Para facilitar o gerenciamento da comunicação de dados entre containers e os nós externos ao ambiente docker, é utilizado uma rede (network) abstrata. Se o sistema será utilizado pela primeira vez no servidor, será necessário realizar essa configuração antes de iniciar os serviços. Para configurar a network que será utilizada pelos containers acesse a raiz do diretório **infra** e execute o script **create-network-docker** que se encontra no arquivo Makefile.


## 1.5.2 Configuração do backend (pokemon)

O projeto do backend foi feito em Python 3.7 utilizando a versão 3.0.3 do framework Django. O gerenciador de banco de dados utilizado no projeto é o Postgres versão 12. Todos estes serviços são executados em containers do Docker, que são instâncias de imagens linux contendo somente os recursos necessários para executar os serviços. Não é necessário a criação do banco de dados, o mesmo será criado quando o container foi iniciado.
Para iniciar a api execute o script **deploy** que está no arquivo Makefile, dentro do diretório infra. O arquivo executado realizará o download das imagens já buildadas da aplicação e que foram armazenados no meu repositório pessoal no registry.gitlab.com. O script realiazará também a configuração de um login inical para que o usuário possa acessar as rotas de listagem dos pokémons e cadastro dos times. Após estes procedimentos a API Restful estará disponível em  http://127.0.0.1:8000.


Para verificar a situação dos serviços executando no docker, utilize o comando abaixo:
>docker ps

# 2. Guia de uso
Para utilizar as rotas da api é necessário gerar um token válido usando os dados de acesso que estão na seção 1.2 e passá-lo no header da request. 
A geração desse token pode ser feita de duas formas:
1. executando o comando abaixo em um terminal bash.

```
     curl \
    -X POST \
    -H "Content-Type: application/json" \
    -d '{"username": "ash", "password": "pickachu"}' \
    http://localhost:8000/core/api/token

```

2. utilizando o arquivo disponibilizado abaixo, basta fazer download do arquivo e abrir em algum aplicativo tipo o Postman.
<adicionar aqui o link do arquivo postman>

## 2.1. Listar pokémons por nome e tipo
A listagem dos pokémons disponíveis pode ser feita acessando a url http://127.0.0.1:8000/core/api/pokemon/?name=nome_pokemon/?types=
todo


## 2.2 Cadastrar times 
todo
