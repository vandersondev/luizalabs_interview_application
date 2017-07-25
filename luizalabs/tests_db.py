#!/usr/bin/env python3


import unittest
from db import getAllPersons, getAllFriends, getAllSuggestions


class TestDb(unittest.TestCase):

    def test_get_all_persons(self):
        persons = getAllPersons()
        self.assertTrue(isinstance(persons, list))
        self.assertEqual(persons[0]['name'], 'Arthur')

    def test_get_all_friends(self):
        friends = getAllFriends('arthur')
        self.assertTrue(isinstance(friends, list))
        self.assertEqual(friends[0]['name'], 'Eduardo')

    def test_get_all_suggestions(self):
        suggestions = getAllSuggestions('arthur')
        self.assertTrue(isinstance(suggestions, list))
        self.assertEqual(suggestions[0]['name'], 'Gabriel')


if __name__ == '__main__':
    unittest.main()
