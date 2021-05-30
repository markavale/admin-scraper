# Generated by Django 3.1.1 on 2021-05-24 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraper', '0029_crawleritem_custom_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='crawleritem',
            name='article_date_created',
        ),
        migrations.AddField(
            model_name='crawleritem',
            name='link_captured',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]