from rest_framework import serializers
from .models import Notification
from api.register.models import Person

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ('id', 'user', 'content', 'quantity', 'notify_date_time', 'created_at')