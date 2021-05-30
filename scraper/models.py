from django.db import models
from django.conf import settings
import math, statistics

User = settings.AUTH_USER_MODEL

status_type = [
    ('Done', 'Done'),
    ('Error', 'Error'),
    ('Processing', 'Processing'),
    ('Queued', 'Queued'),
]

class ScraperAnalysis(models.Model):
    scrapers            = models.ManyToManyField('Scraper')

    class Meta:
        verbose_name_plural = "Scraper Analysis"

    def __str__(self):
        return "Scraper Analysis"

    def get_total_data(self):
        return sum(list(map(lambda scraper: scraper.data, self.scrapers.all())))

    def get_total_articles(self):
        articles_list           = list(map(lambda scraper:scraper.get_total_articles(), self.scrapers.all()))
        return sum(articles_list)
        
    def get_total_avg_dl(self):
        download_latency_list = list(map(lambda scraper: scraper.crawler_set.get_avg_dl_latency(), self.scrapers.all()))
        return round(statistics.mean(download_latency_list), 2)

    def get_total_successfull_parsed(self):
        parsed_article_list     = list(map(lambda scraper: scraper.crawler_set.get_total_parsed_article(), self.scrapers.all()))
        return sum(parsed_article_list)

    def get_total_errors(self):
        # error_list          = list(map(lambda scraper:scraper.crawler_set.get_total_error(), self.scrapers.all()))
        return sum(list(map(lambda scraper:scraper.crawler_set.get_total_error(), self.scrapers.all())))

    def get_total_missed(self):
        missed_article_list         = list(map(lambda scraper: scraper.get_total_missed_articles(), self.scrapers.all()))
        return sum(missed_article_list)
    
    def get_total_rounds_of_scraper(self):
        return self.scrapers.count()

class Scraper(models.Model):
    user                = models.ForeignKey(User, on_delete=models.CASCADE)
    data                = models.IntegerField(default=0)
    workers             = models.IntegerField(default=0)
    spiders             = models.ManyToManyField('ArticleSpider', related_name='spiders_related')
    crawler_set         = models.ForeignKey('CrawlerSet', on_delete=models.CASCADE, blank=True, null=True)
    info_log            = models.TextField(blank=True, null=True)
    error_log           = models.TextField(blank=True, null=True)
    time_finished       = models.TimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
    is_finished         = models.BooleanField(default=False)
    terminated_process  = models.BooleanField(default=False)
    timestamp           = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

    def get_total_spiders(self):
        return self.spiders.count()

    def get_total_threads(self):
        total = 0
        for thread in self.spiders.all():
            total += thread.get_total_thread()
        return total

    def get_total_missed_articles(self):
        data = self.data
        total_articles = self.crawler_set.get_total_articles()
        if data > total_articles:
            return data - total_articles
        else:
            catch_miss_article = self.crawler_set.get_total_parsed_article() + self.crawler_set.get_total_error()
            return total_articles - catch_miss_article

    def get_total_articles(self):
        articles = list(map(lambda article: article.get_total_articles(), self.spiders.all()))
        return sum(articles)

class ArticleSpider(models.Model):
    user                        = models.ForeignKey(User, on_delete=models.CASCADE)
    thread_crawlers             = models.ManyToManyField('ArticleThread')
    in_use                      = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user.username)

    def get_total_thread(self):
        return self.thread_crawlers.count()

    def get_total_articles(self):
        return sum(list(map(lambda article: article.get_total_crawlers(), self.thread_crawlers.all())))
    

class ArticleThread(models.Model):
    user                = models.ForeignKey(User, on_delete=models.CASCADE)
    articles            = models.ManyToManyField('Article')
    in_use              = models.BooleanField(default=False)

    def __str__(self):
        return "Article Thread"

    def get_total_crawlers(self):
        return self.articles.count()

# self relationship
class Article(models.Model):
    url                 = models.URLField()
    article_id          = models.CharField(max_length=255)
    in_use              = models.BooleanField(default=False)

    def __str__(self):
        return self.url

# self relationship
class CrawlerSet(models.Model):
    user                = models.ForeignKey(User, on_delete=models.CASCADE)
    crawlers            = models.ManyToManyField('CrawlerItem')
    is_finished         = models.BooleanField(default=False)
    timestamp           = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return "CrawlerSet"

    def get_total_items(self):
        return self.crawlers.count()

    def get_avg_dl_latency(self):
        total =  0.0
        counter = 0
        items = self.crawlers.all()
        for item in items:
            if item.download_latency is not None:
                counter += 1
                total += item.download_latency
        try:
            avg = total / counter
        except ZeroDivisionError:
            avg = 0
        return round(avg, 2)

    def get_total_http_error(self):
        total = 0
        for error in self.crawlers.all():
            total += error.http_error
        return total
    def get_total_dns_error(self):
        total = 0
        for error in self.crawlers.all():
            total += error.dns_error
        return total
    def get_total_timeout_error(self):
        total = 0
        for error in self.crawlers.all():
            total += error.timeout_error
        return total
    def get_total_base_error(self):
        total = 0
        for error in self.crawlers.all():
            total += error.base_error
        return total
    def get_total_skip_error(self):
        total = 0
        for error in self.crawlers.all():
            total += error.skip_url
        return total
    def get_total_error(self):
        return self.get_total_base_error() + self.get_total_dns_error() + self.get_total_http_error() + self.get_total_timeout_error() + self.get_total_skip_error()
    def get_total_parsed_article(self):
        return self.crawlers.count() - self.get_total_error()
    def get_total_articles(self):
        return self.crawlers.count()
    def get_parsed_percentage(self):
        try:
            part = self.get_total_parsed_article()
            whole = self.get_total_articles()
            return round(100 * float(part)/float(whole), 2)
        except ZeroDivisionError:
            return 0

# self relationship
class CrawlerItem(models.Model):
    article_id              = models.CharField(max_length=255)
    article_url             = models.URLField()
    custom_url              = models.URLField(blank=True, null=True)
    fqdn                    = models.CharField(max_length=255, blank=True, null=True)
    download_latency        = models.FloatField(blank=True, null=True)
    article_status          = models.CharField(max_length=100, choices=status_type)
    article_error_status    = models.CharField(max_length=100, blank=True, null=True)
    link_captured           = models.CharField(max_length=255,null = True, blank = True)
    http_error              = models.IntegerField(default=0)
    dns_error               = models.IntegerField(default=0)
    timeout_error           = models.IntegerField(default=0)
    base_error              = models.IntegerField(default=0)
    skip_url                = models.IntegerField(default=0)   
    timestamp               = models.DateTimeField(auto_now_add=True)
    in_use                  = models.BooleanField(default=False)
    proxy                   = models.CharField(max_length=255,blank=True, null=True)
    user_agent              = models.CharField(max_length=400, blank=True, null=True)
    source_created_from     = models.CharField(max_length=255, blank=True, null=True)
    parser                  = models.CharField(max_length=255, blank=True, null=True)
    handle_httpstatus_list  = models.CharField(max_length=500, blank=True, null=True)
    redirect_urls           = models.CharField(max_length=500, blank=True, null=True)
    redirect_reasons        = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.article_id