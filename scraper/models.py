from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Scraper(models.Model):
    user        = models.ForeignKey(User, on_delete=models.CASCADE)
    data        = models.IntegerField(default=0)
    workers     = models.IntegerField(default=0)
    spiders     = models.ManyToManyField('Spider')
    info_log    = models.TextField(blank=True, null=True)
    error_log   = models.TextField(blank=True, null=True)
    cron_log    = models.TextField(blank=True, null=True)
    is_finish   = models.BooleanField(default=False)
    created     = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

    def total_errors(self):
        total = 0
        for spider in self.spiders.all():
            total += spider.get_total_scraper_errors() 
        return total
    
    def total_skip(self):
        total = 0
        for skip in self.spiders.all():
            total += spder.get_total_skip()
        return total

class Spider(models.Model):
    crawlers            = models.ManyToManyField('SpiderCrawler')


    def get_total_scraper_errors(self):
        total = 0
        for spider in self.crawlers.all():
            total += spider.get_total_errors() 
        return total

    def get_total_skip(self):
        total = 0
        for skip in self.crawlers.all():
            total += spder.skip_url
        return total

    def get_avg_download_latency(self):
        dl_latency = 0
        for latency in self.crawlers.all():
            dl_latency +=latency.download_latency
        avg = dl_latency / self.crawlers.count()
        return avg

class SpiderCrawler(models.Model):
    spider_data         = models.IntegerField(default=0)#ManyToManyField('SpiderUrls')
    download_latency    = models.FloatField()
    http_error          = models.IntegerField(default=0)
    dns_error           = models.IntegerField(default=0)
    timeout_error       = models.IntegerField(default=0)
    base_error          = models.IntegerField(default=0)
    skip_url            = models.IntegerField(default=0)
    is_finish           = models.BooleanField(default=False)

    def __str__(self):
        return "Spider"

    def get_total_errors(self):
        return self.http_error.count() + self.dns_error.count()  + self.timeout_error.count() + self.base_error.count() 
    


# class SpiderUrls(models.Model):
#     url = models.URLField()

#     class Meta:
#         verbose_name_plural = "Spider URLS"

#     def __str__(self):
#         return self.url
