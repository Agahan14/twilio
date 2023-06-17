from rest_framework.views import APIView
from rest_framework.response import Response
from twilio.rest import Client
from django.conf import settings
from rest_framework import viewsets
from .serializers import BannerSerializer
from .models import Banner


class SendSMSView(APIView):
    def post(self, request):
        phone = request.data.get('phone')
        message = request.data.get('message')

        if phone and message:
            try:
                client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
                message = client.messages.create(
                    body=message,
                    from_=settings.TWILIO_PHONE_NUMBER,
                    to=phone
                )
                return Response({'status': 'success', 'message': 'SMS sent successfully.'})
            except Exception as e:
                return Response({'status': 'error', 'message': str(e)})
        else:
            return Response({'status': 'error', 'message': 'Recipient and message are required.'})


class BannerViewSet(viewsets.ModelViewSet):
    serializer_class = BannerSerializer
    queryset = Banner.objects.all()
