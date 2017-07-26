#!/usr/bin/env python3


import unittest
from db import getAllPersons, getAllFriends, getAllSuggestions

'''
Antes de executar o teste

Remova o ponto (caminho relativo) de setting
na linha 2 em db.py

Dá pau com o __name__, eu preferi remover
um ponto do que appendar um path no sys
'''


class TestDb(unittest.TestCase):

    def test_get_all_persons(self):
        persons = getAllPersons()
        list_persons = [i['name'] for i in persons]
        self.assertTrue(isinstance(persons, list))
        self.assertIn('Arthur', list_persons)

    def test_get_all_friends(self):
        friends = getAllFriends('arthur')
        list_friends = [i['name'] for i in friends]
        self.assertTrue(isinstance(friends, list))
        self.assertIn('Eduardo', list_friends)

    def test_get_all_suggestions(self):
        suggestions = getAllSuggestions('arthur')
        list_suggestions = [i['name'] for i in suggestions]
        self.assertTrue(isinstance(suggestions, list))
        self.assertIn('Gabriel', list_suggestions)


if __name__ == '__main__':
    unittest.main()
