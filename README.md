# Plataforma de Voluntariado
Trabalho realizado pela equipe do 8º semestre de Sistemas de Informações do Centro Universitário UNA como Projeto Aplicado do semestre.
A aplicação será uma plataforma web que visa oferecer a voluntários uma forma simples de cadastrarem em oportunidades de voluntariado de sua cidade.

## Tecnologias utilizadas 
A aplicação utilizará as seguintes tecnologias:

* Banco de dados PostgreSQL
* Backend em Python utilizando o Framework Django Rest Framework
* Frontend em Angular6

## Configurando Ambiente da Aplicação

### WINDOWS

* Instale o Python (versão 3.6.5) e garanta que, durante a instalação, você marque nas configurações avançadas a adição do Python à variável PATH do sistema, e instale o Python para todos os usuários
* Instale O PostgreSQL (recomendado: versão 9.5.13) e crie um usuário com username postgres e senha postgres (você pode criar com credenciais diferentes, mas elas terão de ser modificadas no arquivos settings.py do projeto)
* Crie um novo banco de dados chamado appvol. Esse banco de dados deve possuir a collation e character_type Portuguese_Brazil_1252 e tablespace pg_default. Crie atravez da linha de comando ou do PgAdmin.
* Crie uma pasta para o projeto e acesse a pasta
* Instale o Virtualenv através do PIP na linha de comando (pip install virtualenv)
* Crie um ambiente virtual na pasta do projeto através da linha de comando (virtualenv venv)
* Inicie o ambiente virtual na pasta do projeto através da linha de comando (cd env/Scripts/  e depois  activate)
* Crie uma pasta para o aplicativo e acesse a mesma
* Clone o projeto do github na pasta criada
* Instale as dependências do projeto através do PIP (pip install -r requirements.txt)
* Execute os comandos python manage.py makemigrations e python manage.py migrate para criar em seu banco de dados as tabelas do aplicativo*
* Execute o comando python manage.py runserver para executar o servidor

## LINUX

* TODO
