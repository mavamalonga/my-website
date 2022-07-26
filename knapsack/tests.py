# -*- coding: utf-8 -*-
import unittest
from django.test import Client
from django.urls import reverse


class DashboardTest(unittest.TestCase):
    def test_projects(self):
        client = Client()
        response = client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def mentions(self):
        client = Client()
        response = client.get(reverse('mentions-legales'))
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
