from rest_framework import serializers
from .models import UpcomingEvent

class UpcomingEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = UpcomingEvent
        fields = ['id', 'title', 'image', 'start_date', 'end_date', 'location', 'link', 'location_link']
