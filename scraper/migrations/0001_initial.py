# Generated by Django 3.1.1 on 2021-03-14 16:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleSpider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Crawler',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('download_latency', models.FloatField()),
                ('http_error', models.IntegerField(default=0)),
                ('dns_error', models.IntegerField(default=0)),
                ('timeout_error', models.IntegerField(default=0)),
                ('base_error', models.IntegerField(default=0)),
                ('skip_url', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='SpiderCrawler',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_finish', models.BooleanField(default=False)),
                ('crawlers', models.ManyToManyField(to='scraper.Crawler')),
            ],
        ),
        migrations.CreateModel(
            name='Scraper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.IntegerField(default=0)),
                ('workers', models.IntegerField(default=0)),
                ('info_log', models.TextField(blank=True, null=True)),
                ('error_log', models.TextField(blank=True, null=True)),
                ('cron_log', models.TextField(blank=True, null=True)),
                ('is_finish', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('spiders', models.ManyToManyField(to='scraper.ArticleSpider')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='articlespider',
            name='thread_crawlers',
            field=models.ManyToManyField(to='scraper.SpiderCrawler'),
        ),
    ]
