<<<<<<< HEAD
# Generated by Django 5.0.4 on 2024-06-18 22:52
=======
# Generated by Django 5.0.4 on 2024-05-13 23:55
>>>>>>> a49a4dc16ba956fba6e821df7f2174f0cd5b5191

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
<<<<<<< HEAD
        ("login", "0004_alter_loginperson_password_and_more"),
=======
        ('login', '0004_alter_loginperson_password_and_more'),
>>>>>>> a49a4dc16ba956fba6e821df7f2174f0cd5b5191
    ]

    operations = [
        migrations.AlterField(
<<<<<<< HEAD
            model_name="loginperson",
            name="password",
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name="loginperson",
            name="username",
=======
            model_name='loginperson',
            name='password',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='loginperson',
            name='username',
>>>>>>> a49a4dc16ba956fba6e821df7f2174f0cd5b5191
            field=models.CharField(max_length=50),
        ),
    ]
