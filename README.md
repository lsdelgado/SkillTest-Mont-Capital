# SKILL TEST MONT CAPITAL ASSET

## Introdução

Projeto desenvolvido como parte do desafio técnico proposto pela Mont Capital Asset. O objetivo do teste é a obtenção de dados através do consumo da API do IBGE (https://servicodados.ibge.gov.br/api/docs/localidades), organização de dados em DataFrame, geração de um arquivo legível pelo Excel a partir destes dados e criação de uma interface interativa que exiba a quantidade de municípios por estado brasileiro. O back-end da aplicação foi desenvolvido utilizando Python, Django e Django Rest Framework. No front-end foi utilizado HTML, CSS/Bootstrap e Javascript para conferir interatividade e responsividade à página. O banco de dados foi projetado utilizando SQLite.

## Setup

Verifique se tem a versão correta do Python (3.11.5) instalada na sua máquina, além do Django e Django Rest Framework. Ambos podem ser instalados utilizando o comando `pip install django` / `pip install djangorestframework` diretamente no terminal. Esta aplicação roda em um ambiente virtual, então certifique-se de atualizar o arquivo 'pyvenv.cfg' (que pode ser encontrado na pasta '.venv') com as informações da sua máquina. Para ativar o ambiente virtual, escreva o seguinte comando no terminal: 

`venv\Scripts\Activate`

Após a ativação do ambiente, é necessário rodar o servidor. Para fazê-lo, utilize o seguinte comando:

`python manage.py runserver`

## Apps

O aplicativo 'dados' é o responsável pelas funcionalidades da aplicação. A pasta `views.py` contém a implementação das lógicas responsáveis pelas atividades descritas na Introdução. 

Para a obtenção dos dados provenientes do IBGE e criação/atualização de tabela na base de dados, é necessário acessar o endereço `http://127.0.0.1:8000/dados/atualizar_municipios/`. Esta ação gera uma requisição para a view `atualizar_municipios`, que obtém os dados, transforma-os em um DataFrame utilizando a biblioteca pandas e popula a model `Municipios` no banco de dados.

Acessando o endereço `http://127.0.0.1:8000/dados/gerar_csv/`, uma nova requisição get é enviada e esta por sua vez é recebida pela view `gerar_csv`, que transforma os dados do banco de dados (que fora atualizado na ação anterior) em um arquivo no formato csv, legível pelo Excel. 

Para ter acesso à página interativa onde é possível verificar os municípios de cada estado brasileiro, é necessário acessar o endereço `http://127.0.0.1:8000/dados/exibir_municipios/`. A página renderizada exibe os municípios de acordo com o estado selecionado. Foi criada uma API que de acordo com o estado selecionado, filtra e busca os resultados compatíveis no banco de dados e devolve uma lista com os mesmos. Para validar as informações retornadas pela API no formato JSON, acesse `http://127.0.0.1:8000/api/municipios/` para todos os municípios de todos os estados ou `http://127.0.0.1:8000/api/municipios/?uf_sigla=` para filtrar somente os municípios por estado (não se esqueça de colocar a sigla do estado desejado no final da query string).

## Documentação adicional

Para mais informações a respeito das principais tecnologias utilizadas, acesse a documentação oficial:

[Python 3.11.5](https://www.python.org/downloads/release/python-3115/)

[Django](https://docs.djangoproject.com/en/5.0/)

[Django Rest Framework](https://www.django-rest-framework.org/tutorial/quickstart/)


