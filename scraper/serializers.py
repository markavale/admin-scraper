from rest_framework import serializers
from . models import Scraper, ArticleSpider, ArticleThread, Article, CrawlerSet, CrawlerItem

class CrawlerItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = CrawlerItem
        fields = '__all__'

class CrawlerSetSerializer(serializers.ModelSerializer):
    crawlers                                = CrawlerItemSerializer(many=True, read_only=True)
    average_download_latency                = serializers.FloatField(source='get_avg_dl_latency', read_only=True)
    total_http_error                        = serializers.IntegerField(source='get_total_http_error', read_only=True)
    total_dns_error                         = serializers.IntegerField(source='get_total_dns_error', read_only=True)
    total_timeout_error                     = serializers.IntegerField(source='get_total_timeout_error', read_only=True)
    total_base_error                        = serializers.IntegerField(source='get_total_base_error', read_only=True)
    total_skip_error                        = serializers.IntegerField(source='get_total_skip_error', read_only=True)
    total_error                             = serializers.IntegerField(source='get_total_error', read_only=True)
    total_parsed_article                    = serializers.IntegerField(source='get_total_parsed_article', read_only=True)
    total_articles                          = serializers.IntegerField(source='get_total_articles', read_only=True)
    
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
    spiders             = ArticleSpiderSerializer(many=True, read_only=False)
    total_spiders       = serializers.IntegerField(source='get_total_spiders', read_only=True)
    total_threads       = serializers.IntegerField(source='get_total_threads', read_only=True)
    crawler_set         = CrawlerSetSerializer(many=False, read_only=True)

    class Meta:
        model = Scraper
        fields = '__all__'

















