from rest_framework import serializers
from .models import Category, Product, ProductImage, ProductOption

class ProductImageSerializer(serializers.ModelSerializer):
    full_image_url = serializers.SerializerMethodField()

    class Meta:
        model = ProductImage
        fields = ['image', 'alt_text', 'full_image_url']

    def get_full_image_url(self, obj):
        request = self.context.get('request')
        if request:
            return request.build_absolute_uri(obj.image.url)
        return obj.image.url

class ProductOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductOption
        fields = ['name', 'additional_price', 'additional_weight']

class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)
    options = ProductOptionSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'weight', 'get_absolute_url', 'description',
                  'get_image', 'get_thumbnail', 'images', 'options')
        
class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)
    class Meta:
        model = Category
        fields = ('id', 'name', 'get_absolute_url', 'products')