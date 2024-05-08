from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import Person

#Serializer to Register User
class PersonSerializer(serializers.ModelSerializer):
  class Meta:
    model = Person
    fields = ('id', 'username', 'first_name', 'last_name', 'email', 'password', 'confirm_password', 'account_type', 'phone', 'created_by')
    extra_kwargs = {
            'password': {'write_only': True}, 
            'confirm_password': {'write_only': True}
        }
    
  def validate(self, attrs):
    if attrs['password'] != attrs['confirm_password']:
      raise serializers.ValidationError(
        {"confirm_password": "Your passwords didn't match."})
    return attrs
  def create(self, validated_data):
        # Hash the password before saving
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)