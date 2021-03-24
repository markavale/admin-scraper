from django.contrib import admin
from . models import Scraper, ArticleSpider, ArticleThread, Article, CrawlerSet, CrawlerItem

class ScraperAdmin(admin.ModelAdmin):
    list_display = [
        'user', 'data', 'workers', 'crawler_set',
        'time_finished', 'is_finished', 'timestamp'
    ]

class ArticleSpiderAdmin(admin.ModelAdmin):
    list_display = ['user', 'in_use']

class ArticleThreadAdmin(admin.ModelAdmin):
    list_display = ['user', 'in_use']

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['url', 'article_id', 'in_use']

class CrawlerAdmin(admin.ModelAdmin):
    list_display = ['user', 'is_finished', 'timestamp']

class CrawlerItemAdmin(admin.ModelAdmin):
    list_display = ('article_id', 'article_url', 'fqdn', 'download_latency', 'article_status',
                    'article_error_status', 'http_error', 'dns_error', 'timeout_error',
                    'base_error', 'skip_url', 'in_use', 'timestamp',)
    # ordering = ('-date_parsed')


admin.site.register(Scraper, ScraperAdmin)
admin.site.register(ArticleSpider, ArticleSpiderAdmin)
admin.site.register(ArticleThread, ArticleThreadAdmin)
admin.site.register(Article, ArticleAdmin)

admin.site.register(CrawlerSet, CrawlerAdmin)
admin.site.register(CrawlerItem, CrawlerItemAdmin)
