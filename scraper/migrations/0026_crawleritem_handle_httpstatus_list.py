# Generated by Django 3.1.1 on 2021-05-18 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraper', '0025_crawleritem_article_date_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='crawleritem',
            name='handle_httpstatus_list',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]