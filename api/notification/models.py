# notification/models.py
from django.db import models
from api.register.models import Person

class Notification(models.Model):
    user = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='notifications')
    content = models.TextField()
    quantity = models.PositiveIntegerField()
    notify_date_time = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)

