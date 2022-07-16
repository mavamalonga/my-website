# -*- coding: utf-8 -*-
import unittest
from django.test import Client
from django.urls import reverse


class ProjectsTest(unittest.TestCase):
    def test_projects(self):
        """Projects are correctly identified"""
        client = Client()
        response = client.get(reverse('projects'))
        self.assertEqual(response.status_code, 200)

    def test_filter(self):
        client = Client()
        response = client.get('/project/?filter=Python')
        self.assertEqual(response.status_code, 200)

    def test_pagination(self):
        # Curriculum vitae are correctly identified
        client = Client()
        response = client.get('/project/?page=2')
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
