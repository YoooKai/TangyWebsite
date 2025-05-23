from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import UpcomingEvent
from django.urls import reverse

class UpcomingEventAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.event = UpcomingEvent.objects.create(
            title="Evento de prueba",
            start_date="2025-06-01",
            end_date="2025-06-03",
            location="Lugar de prueba",
            link="https://example.com/evento",
            location_link="https://maps.example.com/location"
        )

    def test_upcoming_event_list(self):
        url = reverse('upcoming-events')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(any(event['title'] == "Evento de prueba" for event in response.data))
