#!/usr/bin/env python3


import unittest
import requests
from app import app as my_app


class TestIndexUsingRequests(unittest.TestCase):
    def test_index(self):
        response = requests.get('http://127.0.0.1:5000/')
        self.assertEqual(response.headers['Content-Type'], 'application/json')
        self.assertEqual(response.status_code, 200)


class TestApp(unittest.TestCase):

    def test_index(self):
        app = my_app.test_client()
        response = app.get('/')
        self.assertEqual(response.content_type, 'application/json')


if __name__ == '__main__':
    unittest.main()
