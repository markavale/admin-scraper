# Generated by Django 3.1.1 on 2021-03-21 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraper', '0008_auto_20210321_1351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scraper',
            name='spiders',
            field=models.ManyToManyField(blank=True, null=True, to='scraper.ArticleSpider'),
        ),
    ]