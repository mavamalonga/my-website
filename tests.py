# -*- coding: utf-8 -*-
import unittest
from django.test import Client
from django.urls import reverse


class DashboardTest(unittest.TestCase):
    def test_projects(self):
        client = Client()
        response = client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<title>Lettings</title>', response.content)

    def test_formations(self):
        client = Client()
        response = client.get('index')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<title>Joshua Tree Green Haus /w Hot Tub</title>', response.content)


if __name__ == "__main__":
    unittest.main()