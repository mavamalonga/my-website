# -*- coding: utf-8 -*-
import unittest
from urllib import response
from django.test import Client
from django.urls import reverse


class ProjetsTest(unittest.TestCase):
    def test_projets(self):
        client = Client()
        response = client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<h2 style="font-size:x-large">R\xc3\xa9alisation</h2>', response.content)
"""
    def test_aboutme(self):
        client = Client()
        response = client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<h3 style="font-size: x-large; font-family: Segoe UI, Tahoma, Geneva, Verdana, sans-serif">Me contacter</h3>', response.content)

    def test_skills(self):
        client = Client()
        response = client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(b'<span style="font-size: medium; color: #ff9c00;">Lecture</span>', response.content)

    def test_education(self):
        client = Client()
        response = client.get(reverse('index'))
        self.assertEqual(b'<h2 style="font-size:x-large;">Formations</h2>', response.content)

    def test_hobbies(self):
        client = Client()
        response = client.get(reverse('index'))
        self.assertEqual(b'<h2 style="font-size:x-large; margin-top: 25px;">Hobbies</h2>', response.content)

"""
if __name__ == "__main__":
    unittest.main()