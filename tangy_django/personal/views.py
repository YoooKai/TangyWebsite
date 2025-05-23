from django.http import JsonResponse
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import About, Commissions, FAQ
from .serializers import AboutSerializer, CommissionsSerializer, FAQSerializer
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework import status
from .models import About, Contact


class ContactView(APIView):
    def post(self, request):
            data = request.data
            name = data.get('name')
            email = data.get('email')
            message = data.get('message')

            if not name or not email or not message:
                return Response({'error': 'Todos los campos son obligatorios.'}, status=status.HTTP_400_BAD_REQUEST)

            Contact.objects.create(name=name, email=email, message=message)

            full_message = f"Mensaje de: {name} <{email}>\n\n{message}"

            send_mail(
                subject=f"Nuevo mensaje de {name}",
                message=full_message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.DEFAULT_FROM_EMAIL],
            )

            return Response({'message': '¡Se ha enviado el mensaje con éxito!'}, status=status.HTTP_200_OK)


class AboutView(APIView):
    def get(self, request):
        about = About.objects.first()  # no .all()
        serializer = AboutSerializer(about)
        return Response(serializer.data)

class CommissionsList(APIView):
    def get(self, request):
        commissions = Commissions.objects.all()
        serializer = CommissionsSerializer(commissions, many=True)
        return Response(serializer.data)

class FAQList(APIView):
    def get(self, request):
        faqs = FAQ.objects.all()
        serializer = FAQSerializer(faqs, many=True)
        return Response(serializer.data)