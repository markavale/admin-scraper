from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Scraper(models.Model):
    user            = models.ForeignKey(User, on_delete=models.CASCADE)
    data            = models.IntegerField(default=0)
    workers         = models.IntegerField(default=0)
    spiders         = models.ManyToManyField('ArticleSpider')
    info_log        = models.TextField(blank=True, null=True)
    debug_log       = models.TextField(blank=True, null=True)
    error_log       = models.TextField(blank=True, null=True)
    json_log        = models.TextField(blank=True, null=True)
    is_finished     = models.BooleanField(default=False)
    timestamp       = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

    def get_total_spiders(self):
        return self.spiders.count()

    # def get_total_errors(self):
    #     total = 0
    #     for spider in self.spiders.all():
    #         total += spider.get_total_scraper_errors() 
    #     return total
    
    # def get_total_skip(self):
    #     total = 0
    #     for skip in self.spiders.all():
    #         total += spider.get_total_skip()
    #     return total

    # def get_total_avg_dl_latency(self):
    #     total = 0 
    #     for crawler in self.spiders.all():
    #         total += crawler.article_dl_latencty_avg()
    #     avg = round(total / self.spiders.count(), 2)
    #     return avg

class ArticleSpider(models.Model):
    user                        = models.ForeignKey(User, on_delete=models.CASCADE)
    thread_crawlers             = models.ManyToManyField('SpiderCrawler')
    is_finished                 = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    def get_total_thread(self):
        return self.thread_crawlers.count()

    # def get_total_scraper_errors(self):
    #     total = 0
    #     for spider in self.thread_crawlers.all():
    #         total += spider.get_total_errors() 
    #     return total


class SpiderCrawler(models.Model):
    user                = models.ForeignKey(User, on_delete=models.CASCADE)
    crawlers            = models.ManyToManyField('Crawler')
    is_finished         = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    def get_total_crawlers(self):
        return self.crawlers.count()

class Crawler(models.Model):
    url                 = models.URLField()
    article_id          = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.article_id

class CrawlerSet(models.Model):
    user                = models.ForeignKey(User, on_delete=models.CASCADE)
    crawlers            = models.ManyToManyField('CrawlerItem')

    def __str__(self):
        return self.user.username

class CrawlerItem(models.Model):
    article_id          = models.CharField(max_length=255, blank=True, null=True)
    article_url         = models.URLField()
    download_latency    = models.FloatField()
    http_error          = models.IntegerField(default=0)
    dns_error           = models.IntegerField(default=0)
    timeout_error       = models.IntegerField(default=0)
    base_error          = models.IntegerField(default=0)
    skip_url            = models.IntegerField(default=0)   
    timestamp           = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.article_id