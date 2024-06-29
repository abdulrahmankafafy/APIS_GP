from django.db import models
from api.register.models import Person

class UploadedImage(models.Model):
    image = models.ImageField(upload_to='photos/', null=True)
    predict_value = models.CharField(max_length=255, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

