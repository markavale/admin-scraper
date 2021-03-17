from rest_framework import serializers
from . models import Scraper, ArticleSpider, SpiderCrawler, Crawler


class CrawlerSerializer(serializers.ModelSerializer):
    # spiders = SpiderSerializer()

    class Meta:
        model = Crawler
        fields = '__all__'

class SpiderCrawlerSerializer(serializers.ModelSerializer):
    crawlers = CrawlerSerializer(many=True, read_only=True)

    class Meta:
        model = SpiderCrawler
        fields = '__all__'

class ArticleSpiderSerializer(serializers.ModelSerializer):
    thread_crawlers = SpiderCrawlerSerializer(many=True, read_only=True)
    
    class Meta:
        model = ArticleSpider
        fields = '__all__'


class ScraperSerializer(serializers.ModelSerializer):
    spiders = ArticleSpiderSerializer(many=True, read_only=True)
    total_errors = serializers.IntegerField(source='get_total_errors', read_only=True)
    total_skips = serializers.IntegerField(source='get_total_avg_dl_latency', read_only=True)
    total_dl_latency = serializers.FloatField(source='get_total_avg_dl_latency', read_only=True)


    class Meta:
        model = Scraper
        fields = '__all__'















