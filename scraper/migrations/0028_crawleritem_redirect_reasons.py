# Generated by Django 3.1.1 on 2021-05-18 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraper', '0027_crawleritem_redirect_urls'),
    ]

    operations = [
        migrations.AddField(
            model_name='crawleritem',
            name='redirect_reasons',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
