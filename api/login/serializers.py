from rest_framework import serializers
from .models import LoginPerson
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework import status


class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=50, write_only=True, style={'input_type': 'password'})

    class Meta(object):
        model = LoginPerson
        fields = ["username", "password"]
