# Generated by Django 3.2.18 on 2023-06-11 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0002_guest'),
    ]

    operations = [
        migrations.AddField(
            model_name='guest',
            name='duplicated',
            field=models.BooleanField(default=False),
        ),
    ]