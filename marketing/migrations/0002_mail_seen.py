# Generated by Django 3.1.1 on 2020-11-24 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mail',
            name='seen',
            field=models.BooleanField(default=False),
        ),
    ]
