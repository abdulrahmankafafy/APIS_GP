from django.db import models

class Search(models.Model):
    query = models.TextField()

