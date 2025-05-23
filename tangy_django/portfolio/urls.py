from django.urls import path
from .views import PortfolioEntryList

urlpatterns = [
    path('portfolio/', PortfolioEntryList.as_view(), name='portfolio-list'),
]
