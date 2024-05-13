from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    content= models.TextField()
    published_date=models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.content[:50]