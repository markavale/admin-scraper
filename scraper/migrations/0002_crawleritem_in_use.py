# Generated by Django 3.1.1 on 2021-03-20 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraper', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='crawleritem',
            name='in_use',
            field=models.BooleanField(default=False),
        ),
    ]