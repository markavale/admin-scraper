from rest_framework import serializers
from . models import Scraper, ArticleSpider, ArticleThread, Article, CrawlerSet, CrawlerItem

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

class ArticleSerializer(serializers.ModelSerializer):
    # spiders = SpiderSerializer()

    class Meta:
        model = Article
        fields = '__all__'


class ArticleThreadSerializer(serializers.ModelSerializer):
    articles = ArticleSerializer(many=True, read_only=True)

    class Meta:
        model = ArticleThread
        fields = '__all__'

class ArticleSpiderSerializer(serializers.ModelSerializer):
    thread_crawlers = ArticleThreadSerializer(many=True, read_only=True)
    
    class Meta:
        model = ArticleSpider
        fields = '__all__'


class ScraperSerializer(serializers.ModelSerializer):
    spiders = ArticleSpiderSerializer(many=True, read_only=False)
    total_spiders = serializers.IntegerField(source='get_total_spiders', read_only=True)


    class Meta:
        model = Scraper
        fields = '__all__'

















