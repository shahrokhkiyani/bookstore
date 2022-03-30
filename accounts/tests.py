from urllib import response
from django.test import TestCase
from django.urls import reverse

class SignUpPageTests(TestCase):
    def test_signup_url_by_name(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)



    def test_signup_url(self):
        response = self.client.get('/accounts/signup/')
        self.assertEqual(response.status_code, 200)
        