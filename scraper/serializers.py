from rest_framework import serializers
from . models import Scraper, ArticleSpider, SpiderCrawler, Crawler


class ScraperSerializer(serializers.ModelSerializer):
    spiders = ArticleSpiderSerializer()
    class Meta:
        model = Scraper
        fields = '__all__'

class ArticleSpiderSerializer(serializers.ModelSerializer):
    thread_crawlers = SpiderCrawlerSerializer()
    
    class Meta:
        model = ArticleSpider
        fields = '__all__'

class SpiderCrawlerSerializer(serializers.ModelSerializer):
    crawlers = CrawlerSerializer()

    class Meta:
        model = SpiderCrawler
        fields = '__all__'

class CrawlerSerializer(serializers.ModelSerializer):
    spiders = SpiderSerializer()

    class Meta:
        model = Crawler
        fields = '__all__'


