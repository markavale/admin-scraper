# Generated by Django 3.1.1 on 2021-04-11 14:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scraper', '0022_auto_20210411_1943'),
    ]

    operations = [
        migrations.RenameField(
            model_name='crawleritem',
            old_name='link_created_by',
            new_name='source_created_from',
        ),
    ]
