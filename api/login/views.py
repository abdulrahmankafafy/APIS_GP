
# from django.contrib.auth.hashers import check_password
# from rest_framework import viewsets
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework import permissions
# from .serializers import LoginSerializer
# from django.contrib.auth import authenticate
# from .models import LoginPerson
# from api.register.models import Person

# class LoginView(viewsets.ModelViewSet):
#     queryset = LoginPerson.objects.all()
#     print(Person.objects.all())
#     serializer_class = LoginSerializer
#     permission_classes = [permissions.AllowAny]
#     def post(self, request):
#         serializer = LoginSerializer(data=request.data)
#         if serializer.is_valid():
#             # Get username and password from serializer data
#             username = serializer.validated_data.get('username')
#             password = serializer.validated_data.get('password')

#             # Authenticate user
#             user = authenticate(username=username, password=password)
#             if user is not None:
#                 # Login successful
#                 return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
#             else:
#                 return Response({'error': 'Invalid username or password'}, status=status.HTTP_400_BAD_REQUEST)

#         # If serializer is not valid, return the validation errors
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


from rest_framework import generics, permissions, status, views
from rest_framework.response import Response
from .serializers import LoginSerializer
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import check_password
from api.register.models import Person

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

