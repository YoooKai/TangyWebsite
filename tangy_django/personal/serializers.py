from rest_framework import serializers
from .models import About, Commissions, FAQ

class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = '__all__'
class CommissionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commissions
        fields = '__all__'

class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = '__all__'
