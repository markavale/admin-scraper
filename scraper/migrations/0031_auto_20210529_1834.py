# Generated by Django 3.1.1 on 2021-05-29 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraper', '0030_auto_20210524_1317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crawlerset',
            name='crawlers',
            field=models.ManyToManyField(related_name='crawlers_related', to='scraper.CrawlerItem'),
        ),
        migrations.AlterField(
            model_name='scraper',
            name='spiders',
            field=models.ManyToManyField(related_name='spiders_related', to='scraper.ArticleSpider'),
        ),
    ]
