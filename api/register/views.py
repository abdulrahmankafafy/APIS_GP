from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from django.core.mail import EmailMessage
from django.conf import settings
from django.utils.crypto import get_random_string
from .models import Person
from .serializers import PersonSerializer

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        verification_token = get_random_string(length=32)
        validated_data = serializer.validated_data
        validated_data['email_verification_token'] = verification_token

        if serializer.is_valid():
            serializer.save()
            self.send_verification_email(serializer.instance)

    def send_verification_email(self, instance):
        subject = 'Verify your email address'
        message = f'<p>Click <a href="{settings.BASE_URL}/verify-email/?token={instance.email_verification_token}">here</a> to verify your email address.</p>'
        from_email = settings.DEFAULT_FROM_EMAIL
        to_email = instance.email
        email = EmailMessage(subject, message, from_email, [to_email])
        email.content_subtype = 'html'
        email.send(fail_silently=False)

    def verify_email(self, request):
        token = request.query_params.get('token')

        try:
            person = Person.objects.get(email_verification_token=token)
            person.email_verified = True
            person.email_verification_token = None
            person.save()
            return Response({'message': 'Email verified successfully'}, status=status.HTTP_200_OK)
        except Person.DoesNotExist:
            return Response({'error': 'Invalid verification token'}, status=status.HTTP_400_BAD_REQUEST)