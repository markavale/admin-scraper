# Generated by Django 3.1.1 on 2021-03-24 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraper', '0017_remove_crawleritem_fqdn'),
    ]

    operations = [
        migrations.AddField(
            model_name='crawleritem',
            name='fqdn',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]