from django.test import TestCase, Client
from django.urls import reverse


class IndexViewTestCase(TestCase):

    # Before each test
    def setUp(self):
        self.client = Client()
        self.url = reverse('index')

    # After each test
    def tearDown(self):
        pass

    def test_status_code(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)

    def test_template_used(self):
        response = self.client.get(self.url)

        self.assertTemplateUsed(response, 'index.html')

