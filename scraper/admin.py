from django.contrib import admin
from . models import Scraper, Spider, SpiderCrawler

admin.site.register(Scraper)
admin.site.register(Spider)
admin.site.register(SpiderCrawler)