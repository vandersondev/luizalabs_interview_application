# LuizaLabs Bobby - Desafio

## Instalação

Instale o Neo4j: https://neo4j.com/download/community-edition/

#### Crie um Virtualenv

```
virtualenv bobby
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

No diretório `/luizalabs_interview_application/luizalabs/`, altere o dicionário para as credenciais do seu usuário no banco de dados no arquivo `settings.py`:
```
DATABASES = {
    'user': 'neo4j',
    'passwd': 'root'
}
```

Depois execute o script `load_data.py`:

```
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
flask run
```
## Endpoints

Listar todos os amigos:

```
http://127.0.0.1:5000/friendship/<name>

# por ex: http://127.0.0.1:5000/friendship/arthur
```

Listar todas as sugestões de amigos:

```
http://127.0.0.1:5000/suggestion/<name>

# por ex: http://127.0.0.1:5000/suggestion/gabriel
```

## Créditos

Vanderson Gonçalves - vandersondev@gmail.com
