from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.validators import RegexValidator
from django.utils import timezone


class Person(models.Model):
    x = [
        ('User', 'User'),
        ('Doctor', 'Doctor'),
    ]
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50, validators=[validate_password])
    confirm_password = models.CharField(max_length=50)
    account_type = models.CharField(max_length=50, default='User', choices=x)
    phone = models.CharField(max_length=50, unique=True, validators=[RegexValidator(regex='^[0-9]*$', message='Phone number must contain only digits', code='invalid_phone')])
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE)
    Created_account = models.DateTimeField(default=timezone.now)
    email_verified = models.BooleanField(default=False)
    email_verification_token = models.CharField(max_length=100, null=True, blank=True)
    
    def __str__(self):
        return self.username
