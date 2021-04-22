# Generated by Django 3.1.1 on 2021-03-24 01:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('scraper', '0013_remove_crawleritem_date_parsed'),
    ]

    operations = [
        migrations.AddField(
            model_name='crawlerset',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]