# Generated by Django 3.2.4 on 2023-02-07 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_delete_auditlog'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='geneds',
            field=models.JSONField(null=True),
        ),
    ]