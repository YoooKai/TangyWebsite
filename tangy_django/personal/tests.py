from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import About, Commissions, FAQ, Contact

class PersonalAPITest(APITestCase):
    def setUp(self):
        About.objects.create(title="About Me", content="Descripción personal")
        Commissions.objects.create(title="Commission 1", description="Desc", price=50.00, slots_left=5)
        FAQ.objects.create(question="¿Pregunta?", answer="Respuesta")

    def test_get_about(self):
        url = reverse('about')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('title', response.data)
        self.assertEqual(response.data['title'], "About Me")

    def test_get_commissions(self):
        url = reverse('commissions')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data) > 0)

    def test_get_faq(self):
        url = reverse('faq')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data) > 0)

    def test_post_contact_success(self):
        url = reverse('contact')
        data = {
            'name': 'Sergio',
            'email': 'matraca@example.com',
            'message': 'Hola matraca, este es un mensaje de prueba.'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], '¡Se ha enviado el mensaje con éxito!')
        self.assertTrue(Contact.objects.filter(email='matraca@example.com').exists())

    def test_post_contact_missing_fields(self):
        url = reverse('contact')
        data = {
            'name': '',
            'email': '',
            'message': ''
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('error', response.data)
