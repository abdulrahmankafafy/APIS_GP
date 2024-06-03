from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
import re
from .models import Person

class PersonSerializer(serializers.ModelSerializer):
  password = serializers.CharField(max_length=200, write_only=True, style={'input_type': 'password'})
  confirm_password = serializers.CharField(max_length=50, write_only=True, style={'input_type': 'password'})

  class Meta:
      model = Person
      fields = ('id', 'username', 'first_name', 'last_name', 'email', 'password', 'confirm_password', 'account_type', 'phone')
    
  def validate(self, attrs):
        password = attrs.get('password')
        confirm_password = attrs.get('confirm_password')

        if password and len(password) < 8:
            raise serializers.ValidationError({"password": "Password must be at least 8 characters long."})
        if password and not re.search('[A-Z]', password):
            raise serializers.ValidationError({"password":"Password must contain at least one uppercase letter."})
        if password and not re.search('[0-9]', password):
            raise serializers.ValidationError({"password":"Password must contain at least one digit."})
        if password and not re.search('[^A-Za-z0-9]', password):
            raise serializers.ValidationError({"password":"Password must contain at least one special character."})
        if password != confirm_password:
            raise serializers.ValidationError({"confirm_password": "Your passwords didn't match."})

        return attrs
  def create(self, validated_data):
        confirm_password = validated_data.pop('confirm_password')
        # Hash the password before saving
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)
    
    
    
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
      model = Person
      fields = ('username', 'first_name', 'last_name', 'email', 'phone')
      read_only_fields = ('username')