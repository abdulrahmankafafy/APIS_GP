from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions, status, views
from rest_framework.response import Response
from django.contrib.auth.hashers import check_password, make_password
from api.register.models import Person
from django.core.exceptions import ObjectDoesNotExist
from .serializers import LoginSerializer, ChangePasswordSerializer

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

            if not check_password(password, user.password):
                return Response({'error': 'Invalid password'}, status=status.HTTP_400_BAD_REQUEST)

            return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ChangePasswordConfirmView(views.APIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = ChangePasswordSerializer

    def post(self, request, *args, **kwargs):
        serializer = ChangePasswordSerializer(data=request.data)

        if serializer.is_valid():
            username = serializer.validated_data.get('username')
            try:
                user = Person.objects.get(username=username)
            except Person.DoesNotExist:
                return Response({'error': 'User does not exist.'}, status=status.HTTP_400_BAD_REQUEST)

            old_password = serializer.validated_data.get('old_password')
            if not check_password(old_password, user.password):
                return Response({'error': 'Incorrect old password.'}, status=status.HTTP_400_BAD_REQUEST)

            new_password = serializer.validated_data.get('new_password')
            print(new_password)
            print(old_password)
            if  old_password == new_password:
                return Response({'error': 'The new password matches the old password, please enter a different password.'}, status=status.HTTP_400_BAD_REQUEST)
            user.password = make_password(new_password)
            user.save()
            return Response({'message': 'Password changed successfully.'}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

