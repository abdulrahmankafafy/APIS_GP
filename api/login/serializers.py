from rest_framework import serializers
from .models import LoginPerson
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ValidationError
import re


class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=50, write_only=True, style={'input_type': 'password'})

    class Meta(object):
        model = LoginPerson
        fields = ["username", "password"]


# class ChangePasswordSerializer(serializers.Serializer):
#     old_password = serializers.CharField(required=True)
#     new_password = serializers.CharField(required=True)
    
#     def validate(self, attrs):
#         new_password = attrs.get('new_password')

#         if new_password and len(new_password) < 8:
#             raise serializers.ValidationError({"New password": "password must be at least 8 characters long."})
#         if new_password and not re.search('[A-Z]', new_password):
#             raise serializers.ValidationError({"New password":"password must contain at least one uppercase letter."})
#         if new_password and not re.search('[0-9]', new_password):
#             raise serializers.ValidationError({"New password":"password must contain at least one digit."})
#         if new_password and not re.search('[^A-Za-z0-9]', new_password):
#             raise serializers.ValidationError({"New password":"password must contain at least one special character."})
#         return attrs
    
    
# class ResetPasswordEmailSerializer(serializers.Serializer):
#     email = serializers.EmailField(required=True)
