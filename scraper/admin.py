from django.contrib import admin
from . models import Scraper, ArticleSpider, SpiderCrawler, Crawler





admin.site.register(Scraper)
admin.site.register(ArticleSpider)
admin.site.register(SpiderCrawler)
admin.site.register(Crawler)