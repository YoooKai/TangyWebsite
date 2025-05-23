from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.urls import reverse
from .models import Order, OrderItem
from product.models import Product, Category

class OrderAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        self.category = Category.objects.create(name="Test Category", slug="test-category")
        self.product = Product.objects.create(
            category=self.category,
            name="Test Product",
            slug="test-product",
            price=10.00,
            weight=100
        )

    def test_checkout_success(self):
        url = reverse('checkout')  

        data = {
            "first_name": "Sergio",
            "last_name": "Delgado",
            "email": "matraca@example.com",
            "address": "123 Matracazo",
            "zipcode": "12345",
            "place": "City",
            "phone": "1234567890",
            "stripe_token": "tok_visa", 
            "shipping_cost": "5.00",
            "items": [
                {
                    "product": self.product.id,
                    "quantity": 2,
                    "price": "10.00"
                }
            ]
        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Order.objects.count(), 1)
        self.assertEqual(OrderItem.objects.count(), 1)
        self.assertEqual(Order.objects.first().paid_amount, 25.00)  

    def test_checkout_missing_fields(self):
        url = reverse('checkout')

        data = {
            "first_name": "Sergio",
            "stripe_token": "tok_visa",
            "items": []
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_orders_list(self):
        order = Order.objects.create(
            user=self.user,
            first_name="Sergio",
            last_name="Doe",
            email="matraca@example.com",
            address="123 Matracazo",
            zipcode="12345",
            place="City",
            phone="1234567890",
            stripe_token="tok_visa",
            paid_amount=15.00
        )
        response = self.client.get(reverse('orders-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
