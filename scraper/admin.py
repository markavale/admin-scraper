from django.contrib import admin
from . models import Scraper, ArticleSpider, ArticleThread, Article, CrawlerSet, CrawlerItem





admin.site.register(Scraper)
admin.site.register(ArticleSpider)
admin.site.register(ArticleThread)
admin.site.register(Article)

admin.site.register(CrawlerSet)
admin.site.register(CrawlerItem)