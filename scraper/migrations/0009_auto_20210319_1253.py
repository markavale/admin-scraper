# Generated by Django 3.1.1 on 2021-03-19 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraper', '0008_auto_20210319_1049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crawler',
            name='article_id',
            field=models.CharField(default='60508223b5095b393dc3fb03', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='crawleritem',
            name='article_id',
            field=models.CharField(default='60508223b5095b393dc3fb03', max_length=255),
            preserve_default=False,
        ),
    ]
