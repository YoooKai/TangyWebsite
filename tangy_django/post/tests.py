from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import Post

class PostAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.post = Post.objects.create(
            title="Test Post",
            content="Contenido de prueba para el post.",
            category=Post.Category.ANNOUNCEMENT
        )

    def test_post_list(self):
        """Comprueba que la lista de posts responde correctamente."""
        response = self.client.get('/api/v1/posts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(any(p['title'] == "Test Post" for p in response.data))

    def test_post_detail(self):
        """Comprueba que el detalle del post responde correctamente."""
        response = self.client.get(f'/api/v1/posts/{self.post.slug}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "Test Post")

    def test_post_not_found(self):
        """Comprueba que devuelve 404 si el post no existe."""
        response = self.client.get('/api/v1/posts/slug-inexistente/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
