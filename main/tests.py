from django.test import TestCase
from django.test import SimpleTestCase


class SimpleTestCase(SimpleTestCase):
    def test_home_page_status_code(self):
        respomse = self.client.get('/')
        self.assertEqual(respomse.status_code, 200)

    def test_home_page_status_code(self):
        respomse = self.client.get('/about/')
        self.assertEqual(respomse.status_code, 200)
