from django.urls import path
from .views import UpcomingEventList

urlpatterns = [
    path('events/', UpcomingEventList.as_view(), name='upcoming-events'),
]
