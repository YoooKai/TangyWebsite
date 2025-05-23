from django.urls import path
from .views import ContactView, AboutView, CommissionsList, FAQList

urlpatterns = [
    path('contact/', ContactView.as_view(), name='contact'),
    path('about/', AboutView.as_view(), name='about'),
    path('commissions/', CommissionsList.as_view(), name='commissions'),
    path('faq/', FAQList.as_view(), name='faq'),
]
