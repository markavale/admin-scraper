from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

status_type = [
    ('Done', 'Done'),
    ('Error', 'Error'),
    ('Processing', 'Processing'),
    ('Queued', 'Queued'),
]

class Scraper(models.Model):
    user            = models.ForeignKey(User, on_delete=models.CASCADE)
    data            = models.IntegerField(default=0)
    workers         = models.IntegerField(default=0)
    spiders         = models.ManyToManyField('ArticleSpider')
    crawler_set     = models.ForeignKey('CrawlerSet', on_delete=models.CASCADE, blank=True, null=True)
    info_log        = models.TextField(blank=True, null=True)
    error_log       = models.TextField(blank=True, null=True)
    time_finished   = models.TimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
    is_finished     = models.BooleanField(default=False)
    timestamp       = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

    def get_total_spiders(self):
        return self.spiders.count()

class ArticleSpider(models.Model):
    user                        = models.ForeignKey(User, on_delete=models.CASCADE)
    thread_crawlers             = models.ManyToManyField('ArticleThread')
    in_use                      = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user.username)

    def get_total_thread(self):
        return self.thread_crawlers.count()

class ArticleThread(models.Model):
    user                = models.ForeignKey(User, on_delete=models.CASCADE)
    articles            = models.ManyToManyField('Article')
    in_use              = models.BooleanField(default=False)

    def __str__(self):
        return "Article Thread"

    def get_total_crawlers(self):
        return self.articles.count()

class Article(models.Model):
    url                 = models.URLField()
    article_id          = models.CharField(max_length=255)
    in_use              = models.BooleanField(default=False)

    def __str__(self):
        return self.url

class CrawlerSet(models.Model):
    user                = models.ForeignKey(User, on_delete=models.CASCADE)
    crawlers            = models.ManyToManyField('CrawlerItem')
    is_finished         = models.BooleanField(default=False)
    timestamp           = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return "CrawlerSet"

    def get_total_items(self):
        return self.crawlers.count()

class CrawlerItem(models.Model):
    article_id              = models.CharField(max_length=255)
    article_url             = models.URLField()
    # fqdn                    = models.CharField(max_length=255, blank=True, null=True)
    download_latency        = models.FloatField(blank=True, null=True)
    article_status          = models.CharField(max_length=100, choices=status_type)
    article_error_status    = models.CharField(max_length=100, blank=True, null=True)
    http_error              = models.IntegerField(default=0)
    dns_error               = models.IntegerField(default=0)
    timeout_error           = models.IntegerField(default=0)
    base_error              = models.IntegerField(default=0)
    skip_url                = models.IntegerField(default=0)   
    timestamp               = models.DateTimeField(auto_now_add=True)
    in_use                  = models.BooleanField(default=False)

    def __str__(self):
        return self.article_id