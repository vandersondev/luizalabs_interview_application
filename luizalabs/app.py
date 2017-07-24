from flask import Flask
from flask_restful import Api, Resource
import logging
from .db import getAllFriends, getAllPersons, getAllSuggestions

app = Flask('luizalabs')
api = Api(app)

logging.basicConfig(filename='app.log', level=logging.DEBUG)


class Index(Resource):
    def get(self):
        logging.info('Listando todos as Pessoas')
        persons = getAllPersons()

        return persons


class Friendship(Resource):
    def get(self, name):
        logging.info('Listando todos as amizades de {}'.format(name))
        friends = getAllFriends(name)

        return friends


class Suggestion(Resource):
    def get(self, name):

        logging.info('Listando todas as recomendações de {}'.format(name))
        suggestions = getAllSuggestions(name)

        return suggestions


api.add_resource(Index, '/')
api.add_resource(Friendship, '/friendship/<string:name>')
api.add_resource(Suggestion, '/suggestion/<string:name>')
