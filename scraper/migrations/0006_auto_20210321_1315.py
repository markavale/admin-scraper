# Generated by Django 3.1.1 on 2021-03-21 05:15

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('scraper', '0005_auto_20210320_2256'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Crawler',
            new_name='Article',
        ),
        migrations.RenameModel(
            old_name='SpiderCrawler',
            new_name='ArticleThread',
        ),
    ]
