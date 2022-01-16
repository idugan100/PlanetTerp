# Generated by Django 3.2.4 on 2022-01-15 22:56

import django.contrib.auth.validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0041_alter_user_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(help_text='Once a username is set, it cannot be changed.', max_length=20, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator(), django.core.validators.MaxLengthValidator(20, 'Username must be less than 20 characters'), django.core.validators.MinLengthValidator(2, 'Username must be at least 2 characters')]),
        ),
    ]