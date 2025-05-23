from rest_framework.views import APIView
from rest_framework.response import Response
from .models import UpcomingEvent
from .serializers import UpcomingEventSerializer

class UpcomingEventList(APIView):
    def get(self, request, format=None):
        events = UpcomingEvent.objects.all()
        serializer = UpcomingEventSerializer(events, many=True)
        return Response(serializer.data)
