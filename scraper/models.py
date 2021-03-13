from django.db import models

# from django.conf import settings

class Scraper(models.Model):
    spiders = models.ManyToManyField('Spider')
    is_finish = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.created + " " + self.spiders.count()

    def get_total_scraper_errors(self):
        total = 0
        for spider in self.spiders.all:
            total += spider.get_total_errors 
        return total

class Spider(models.Model):
    spider_urls     = models.ManyToManyField('SpiderUrls')
    http_error      = models.IntegerField(default=0)
    dns_error       = models.IntegerField(default=0)
    timeout_error   = models.IntegerField(default=0)
    base_error      = models.IntegerField(default=0)
    is_finish       = models.BooleanField(default=False)

    def __str__(self):
        return "Spider"

    def get_total_errors(self):
        return self.http_error.count() + self.dns_error.count()  + self.timeout_error.count() + self.base_error.count() 
    


class SpiderUrls(models.Model):
    url = models.URLField()

    class Meta:
        verbose_name_plural = "Spider URLS"

    def __str__(self):
        return self.url
