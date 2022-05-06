from urllib import response
from django.test import TestCase
from django.urls import include, path, reverse
from rest_framework.test import APITestCase, URLPatternsTestCase
from rest_framework import status
# Create your tests here.

class AppTests(APITestCase, URLPatternsTestCase):
    urlpatterns = [
        path('api/',include('api.urls')),
    ]
    def test_ping_response(self):
        """
        Test ping feature works
        """
        response = self.client.get("http://localhost:8000/api/ping/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    def test_ping_body(self):
        """
        Test ping feature works
        """
        response = self.client.get("http://localhost:8000/api/ping/")
        self.assertEqual(response.content, b'{"success": true}')
    def test_bad_method_ping_response(self):
        """
        Test ping feature works
        """
        response = self.client.post("http://localhost:8000/api/ping/")
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
    def test_
