# Generated by Django 3.1.1 on 2021-03-24 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraper', '0015_crawleritem_fqdn'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crawleritem',
            name='fqdn',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
