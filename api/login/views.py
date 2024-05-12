from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions, status, views
from rest_framework.response import Response
from django.contrib.auth.hashers import check_password
from api.register.models import Person
from django.contrib.auth import update_session_auth_hash
from .serializers import LoginSerializer

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
    
# class PasswordResetConfirmView(views.APIView):
#     permission_classes = (permissions.AllowAny, )
#     serializer_class = ChangePasswordSerializer

#     def post(self, request, *args, **kwargs):
#         serializer = ChangePasswordSerializer(data=request.data)
#         print(request.user)
#         if serializer.is_valid():
#             # Check if the user is authenticated
#             if request.user.is_authenticated:
#                 user = request.user
#                 if user.check_password(serializer.data.get('old_password')):
#                     user.set_password(serializer.data.get('new_password'))
#                     user.save()
#                     update_session_auth_hash(request, user)  # To update session after password change
#                     return Response({'message': 'Password changed successfully.'}, status=status.HTTP_200_OK)
#                 return Response({'error': 'Incorrect old password.'}, status=status.HTTP_400_BAD_REQUEST)
#             else:
#                 return Response({'error': 'Authentication credentials were not provided.'}, status=status.HTTP_401_UNAUTHORIZED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


