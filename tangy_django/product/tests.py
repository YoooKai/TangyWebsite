from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Category, Product

class ProductAPITest(APITestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Test Category", slug="test-category")
        self.product = Product.objects.create(
            category=self.category,
            name="Test Product",
            slug="test-product",
            price=9.99,
            weight=100
        )

    def test_latest_products_list(self):
        url = reverse('latest-products')
        response = self.client.get('/api/v1/latest-products/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(any(p['name'] == "Test Product" for p in response.data))

    def test_product_detail(self):
        url = f'/api/v1/products/{self.category.slug}/{self.product.slug}/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], "Test Product")

    def test_category_detail(self):
        url = f'/api/v1/products/{self.category.slug}/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], "Test Category")
        self.assertTrue('products' in response.data)

    def test_search_products(self):
        url = '/api/v1/products/search/'
        response = self.client.post(url, {'query': 'Test'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(any(p['name'] == "Test Product" for p in response.data))

    def test_search_no_query(self):
        url = '/api/v1/products/search/'
        response = self.client.post(url, {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['products'], [])
