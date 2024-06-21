from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import permissions, status, views
from django.core.mail import EmailMessage
from django.conf import settings
from django.utils.crypto import get_random_string
from .models import Person
from .serializers import PersonSerializer, ProfileSerializer
class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True) 
        verification_token = get_random_string(length=32)
        serializer.validated_data['email_verification_token'] = verification_token
        # serializer.validated_data['is_logged_in'] = True
        instance = serializer.save()
        self.send_verification_email(instance)
        return Response({'message': 'User registered successfully'}, status=status.HTTP_200_OK)
    
    def send_verification_email(self, instance):
        subject = 'Verify your email address'
        message = f'<p>Click <a href="{settings.BASE_URL}/verify_email/?token={instance.email_verification_token}">here</a> to verify your email address.</p>'
        to_email = instance.email
        email = EmailMessage(subject, message, to=[to_email])
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
        

class LogoutView(views.APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, person_id):
        try:
            user = Person.objects.get(id=person_id)
        except Person.DoesNotExist:
            return Response({'error': 'User does not exist'}, status=status.HTTP_404_NOT_FOUND)
        
        if not user.is_logged_in:
            return Response({'error': 'User is already logged out'}, status=status.HTTP_403_FORBIDDEN)

        user.is_logged_in = False
        user.save()
        return Response({'message': 'Logout successful'}, status=status.HTTP_200_OK)
    


class ProfileView(views.APIView):
    serializer_class = ProfileSerializer
    permission_classes = [permissions.AllowAny]

    def get(self, request, person_id):
        try:
            user = Person.objects.get(id=person_id)
        except Person.DoesNotExist:
            return Response({'error': 'User does not exist'}, status=status.HTTP_404_NOT_FOUND)
        
        if not user.is_logged_in:
            return Response({'error': 'User is not logged in'}, status=status.HTTP_403_FORBIDDEN)
        
        serializer = ProfileSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, username):
        try:
            user = Person.objects.get(username=username)
        except Person.DoesNotExist:
            return Response({'error': 'User does not exist'}, status=status.HTTP_404_NOT_FOUND)

        if user.username != username:
            return Response({'error': 'You cannot edit your username.'}, status=status.HTTP_403_FORBIDDEN)

        serializer = ProfileSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            
            if not user.is_logged_in:
                return Response({'error': 'User is not logged in'}, status=status.HTTP_403_FORBIDDEN)
            
            new_email = serializer.validated_data.get('email')
            if new_email and Person.objects.exclude(username=username).filter(email=new_email).exists():
                return Response({'error': 'This email is already in use by another user.'}, status=status.HTTP_400_BAD_REQUEST)

            new_phone = serializer.validated_data.get('phone')
            if new_phone and Person.objects.exclude(username=username).filter(phone=new_phone).exists():
                return Response({'error': 'This phone number is already in use by another user.'}, status=status.HTTP_400_BAD_REQUEST)

            user.first_name = serializer.validated_data.get('first_name', user.first_name)
            user.last_name = serializer.validated_data.get('last_name', user.last_name)
            user.email = serializer.validated_data.get('email', user.email)
            user.phone = serializer.validated_data.get('phone', user.phone)
            user.save()

            return Response({'message': 'The profile has been successfully updated'}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)