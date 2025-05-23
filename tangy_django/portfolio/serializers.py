from rest_framework import serializers
from .models import PortfolioEntry

class PortfolioEntrySerializer(serializers.ModelSerializer):
    category_display = serializers.CharField(source='get_category_display', read_only=True)

    class Meta:
        model = PortfolioEntry
        fields = ['id', 'title', 'image', 'category', 'category_display', 'created_at']
