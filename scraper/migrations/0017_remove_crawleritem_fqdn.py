# Generated by Django 3.1.1 on 2021-03-24 10:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scraper', '0016_auto_20210324_1832'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='crawleritem',
            name='fqdn',
        ),
    ]
