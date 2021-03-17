from django.contrib import admin
from . models import Scraper, ArticleSpider, SpiderCrawler, Crawler, CrawlerSet, CrawlerItem





admin.site.register(Scraper)
admin.site.register(ArticleSpider)
admin.site.register(SpiderCrawler)
admin.site.register(Crawler)

admin.site.register(CrawlerSet)
admin.site.register(CrawlerItem)