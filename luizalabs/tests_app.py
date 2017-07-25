#!/usr/bin/env python3


import unittest
import requests
import json


class TestAppUsingRequests(unittest.TestCase):

    def setUp(self):
        self.request = requests

    def test_can_list_index(self):
        response = self.request.get('http://127.0.0.1:5000/')
        persons = json.loads(response.content.decode('utf-8'))
        self.assertEqual(response.headers['Content-Type'], 'application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(persons[0]['name'], 'Arthur')

    def test_can_list_friendship(self):
        response = self.request.get('http://127.0.0.1:5000/friendship/arthur')
        friends = json.loads(response.content.decode('utf-8'))
        self.assertEqual(response.headers['Content-Type'], 'application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(friends[0]['name'], 'Eduardo')

    def test_can_list_suggestions(self):
        response = self.request.get('http://127.0.0.1:5000/suggestion/arthur')
        friends = json.loads(response.content.decode('utf-8'))
        self.assertEqual(response.headers['Content-Type'], 'application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(friends[0]['name'], 'Gabriel')


if __name__ == '__main__':
    unittest.main()
