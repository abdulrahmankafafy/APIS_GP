# Generated by Django 5.0.4 on 2024-05-08 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_remove_person_confirm_password_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='confirm_password',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='password',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
