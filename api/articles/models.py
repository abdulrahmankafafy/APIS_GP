from django.db import models
from django.utils import timezone
from api.register.models import Person  # Assuming Person model is in the register app

class Article(models.Model):
    author = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='articles')
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
