# Generated by Django 5.0.4 on 2024-06-03 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0004_remove_person_is_logged_in'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='is_logged_in',
            field=models.BooleanField(default=False),
        ),
    ]
