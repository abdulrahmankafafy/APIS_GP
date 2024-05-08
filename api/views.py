from rest_framework import viewsets
from .serializers import PersonSerializer
from .models import Person
from django.core.mail import EmailMessage
from django.conf import settings
from rest_framework.response import Response
from rest_framework import status
from django.utils.crypto import get_random_string
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ValidationError

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    def perform_create(self, serializer):
        verification_token = get_random_string(length=32)
        validated_data = serializer.validated_data
        validated_data['email_verification_token'] = verification_token
        
        try:
            print(serializer.save())
            self.send_verification_email(serializer.instance)
        except ValidationError as ve:
            error_message = f"Error saving {validated_data.get('username')}: {ve}"
            return Response({"error": error_message}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            error_message = f"Error saving {validated_data.get('username')}: {e}"
            return Response({"error": error_message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def send_verification_email(self, instance):
     subject = 'Verify your email address'
     message = f'<p>Click <a href="{settings.BASE_URL}/verify-email?token={instance.email_verification_token}">here</a> to verify your email address.</p>'
     from_email = settings.DEFAULT_FROM_EMAIL
     to_email = instance.email
     email = EmailMessage(subject, message, from_email, [to_email])
     email.content_subtype = 'html'
     email.send(fail_silently=False)


    def verify_email(self, request):
        token = request.query_params.get('token')
        try:
            person = Person.objects.get(email_verification_token=token)
        except Person.DoesNotExist:
            return Response({'error': 'Invalid verification token'}, status=status.HTTP_400_BAD_REQUEST)
        
        person.email_verified = True
        person.email_verification_token = None
        person.save()
        return Response({'message': 'Email verified successfully'}, status=status.HTTP_200_OK)
