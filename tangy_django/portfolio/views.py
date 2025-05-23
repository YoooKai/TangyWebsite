from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from .models import PortfolioEntry
from .serializers import PortfolioEntrySerializer

class PortfolioEntryList(APIView):
    def get(self, request, format=None):
        category = request.GET.get('category', None)
        entries = PortfolioEntry.objects.all()
        if category:
            entries = entries.filter(category=category)
        serializer = PortfolioEntrySerializer(entries, many=True)
        return Response(serializer.data)
