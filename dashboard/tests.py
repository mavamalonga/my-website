# -*- coding: utf-8 -*-
import unittest
from django.test import Client
from django.urls import reverse


class DashboardTest(unittest.TestCase):
    def test_top_projects(self):
        """TOP projects are are correctly identified"""
        client = Client()
        response = client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<h5>My-Portfolio</h5>', response.content)
        self.assertIn(b'<h5>SoftDesk</h5>', response.content)

    def test_degrees(self):
        client = Client()
        response = client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<small class="text-muted"><b>Paris 2020-2022</b></small>', response.content)

    def test_curriculum_vitae(self):
        """Curriculum vitae are correctly identified"""
        client = Client()
        response = client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Curriculum vitae', response.content)

if __name__ == "__main__":
    unittest.main()