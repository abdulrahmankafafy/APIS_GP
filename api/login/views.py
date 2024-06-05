from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions, status, views
from rest_framework.response import Response
from django.core.mail import EmailMessage
from django.conf import settings
from django.urls import reverse
from django.contrib.auth.hashers import check_password, make_password
from django.utils.crypto import get_random_string
from api.register.models import Person
from .serializers import LoginSerializer, ChangePasswordSerializer, ForgetPasswordSerializer, ResetPasswordSerializer

class LoginView(views.APIView):
    permission_classes = (permissions.AllowAny, )
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data.get('username')
            password = serializer.validated_data.get('password')
            try:
                user = Person.objects.get(username=username)
            except Person.DoesNotExist:
                return Response({'error': 'User does not exist'}, status=status.HTTP_400_BAD_REQUEST)
            
            if user.is_logged_in:
                return Response({'error': 'User is already logged in'}, status=status.HTTP_400_BAD_REQUEST)

            if not check_password(password, user.password):
                return Response({'error': 'Invalid password'}, status=status.HTTP_400_BAD_REQUEST)
            
            user.is_logged_in = True
            user.save()
            response_data = {
                'message': 'Login successful',
                'username': user.username,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'email': user.email,
                'phone': user.phone,
            }
            return Response(response_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ChangePasswordConfirmView(views.APIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = ChangePasswordSerializer

    def post(self, request, username, *args, **kwargs):
        serializer = ChangePasswordSerializer(data=request.data)

        if serializer.is_valid():
            try:
                user = Person.objects.get(username=username)
            except Person.DoesNotExist:
                return Response({'error': 'User does not exist.'}, status=status.HTTP_400_BAD_REQUEST)

            if not user.is_logged_in:
                return Response({'error': 'User is not logged in.'}, status=status.HTTP_400_BAD_REQUEST)
            
            old_password = serializer.validated_data.get('old_password')
            if not check_password(old_password, user.password):
                return Response({'error': 'Incorrect old password.'}, status=status.HTTP_400_BAD_REQUEST)

            new_password = serializer.validated_data.get('new_password')
            if  old_password == new_password:
                return Response({'error': 'The new password matches the old password, please enter a different password.'}, status=status.HTTP_400_BAD_REQUEST)
            user.password = make_password(new_password)
            user.save()
            return Response({'message': 'Password changed successfully.'}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class ForgetPasswordView(views.APIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = ForgetPasswordSerializer

    def post(self, request, *args, **kwargs):
        serializer = ForgetPasswordSerializer(data=request.data)

        if serializer.is_valid():
            email = serializer.validated_data.get('email')
            try:
                person = Person.objects.get(email=email)
            except Person.DoesNotExist:
                return Response({'error': 'Email address not found.'}, status=status.HTTP_404_NOT_FOUND)

            verification_token = get_random_string(length=32)
            person.email_verification_token = verification_token
            person.save()
            self.send_verification_email_reset_password(person.email, person.email_verification_token)
            
            return Response({'message': 'Email sent successfully.'}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def send_verification_email_reset_password(self, email, token):
        subject = 'Reset your password'
        message = f'<p>Click <a href="{settings.BASE_URL}/login/reset_password/?token={token}">here</a> to reset your password.</p>'
        to_email = email
        email = EmailMessage(subject, message, [to_email])
        email.content_subtype = 'html'
        email.send(fail_silently=False)


class ResetPasswordView(views.APIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = ResetPasswordSerializer

    def post(self, request, *args, **kwargs):
        token = request.query_params.get('token')
        try:
            person = Person.objects.get(email_verification_token=token)
        except Person.DoesNotExist:
            return Response({'error': 'Invalid reset password token.'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = ResetPasswordSerializer(data=request.data)
        if serializer.is_valid():
            new_password = serializer.validated_data.get('new_password')

            person.password = make_password(new_password)
            person.email_verification_token = None
            person.save()

            return Response({'message': 'Password reset successfully.'}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
