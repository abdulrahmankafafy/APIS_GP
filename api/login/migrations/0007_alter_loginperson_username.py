# Generated by Django 5.0.4 on 2024-05-14 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0006_alter_loginperson_password_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loginperson',
            name='username',
            field=models.CharField(max_length=50),
        ),
    ]