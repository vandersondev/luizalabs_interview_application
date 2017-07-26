# LuizaLabs Bobby - Desafio

## Instalação

#### Crie um Virtualenv

```
virtualenv -p python3 ENV
source bin/activate
```
#### Clone o projeto

```
git clone git@github.com:vandersondev/luizalabs_interview_application.git
```

#### Instale as dependências

```
cd luizalabs_interview_application
pip install -r requirements.txt
```
#### Crie a estrutura no Neo4j

```
cd luizalabs
python load_data.py
```

Para criar as arestas de sugestões de amigos:

```
python suggestions.py
```

## Utilização

No diretório `/luizalabs_interview_application/luizalabs/`

```
export FLASK_APP=app.py
flaks run
```
