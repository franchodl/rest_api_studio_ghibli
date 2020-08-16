from django.test import SimpleTestCase, TestCase
from django.urls import reverse

from . import views

# Create your tests here.

class MoviesTests(SimpleTestCase):

    def test_found(self):
        response = self.client.get('/movies/')
        self.assertEquals(response.status_code, 200)

    def test_template(self):
        self.assertTemplateUsed(self.client.get('/movies/'), 'movies/movies.html')

