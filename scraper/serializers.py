from rest_framework import serializers
from . models import Scraper, ArticleSpider, SpiderCrawler, Crawler, CrawlerSet, CrawlerItem


class CrawlerItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = CrawlerItem
        fields = '__all__'

class CrawlerSetSerializer(serializers.ModelSerializer):
    crawlers        = CrawlerItemSerializer(many=True, read_only=True)

    class Meta:
        model = CrawlerSet
        fields = '__all__'
### 

class CrawlerSerializer(serializers.ModelSerializer):
    # spiders = SpiderSerializer()

    class Meta:
        model = Crawler
        fields = '__all__'


class SpiderCrawlerSerializer(serializers.ModelSerializer):
    crawlers = CrawlerSerializer(many=True, read_only=True)
    crawler_set = CrawlerSetSerializer(many=True, read_only=True)
    class Meta:
        model = SpiderCrawler
        fields = '__all__'

class ArticleSpiderSerializer(serializers.ModelSerializer):
    thread_crawlers = SpiderCrawlerSerializer(many=True, read_only=True)
    
    class Meta:
        model = ArticleSpider
        fields = '__all__'


class ScraperSerializer(serializers.ModelSerializer):
    spiders = ArticleSpiderSerializer(many=True, read_only=False)
    total_spiders = serializers.IntegerField(source='get_total_spiders', read_only=True)


    class Meta:
        model = Scraper
        fields = '__all__'

















