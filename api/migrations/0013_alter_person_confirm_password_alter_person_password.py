# Generated by Django 5.0.4 on 2024-05-08 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_person_confirm_password_person_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='confirm_password',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='password',
            field=models.CharField(max_length=50, null=True),
        ),
    ]