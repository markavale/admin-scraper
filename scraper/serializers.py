from rest_framework import serializers
from . models import Scraper, Spider, SpiderUrls




class SpiderUrlsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = SpiderUrls
        fields = '__all__'

class SpiderSerializer(serializers.ModelSerializer):
    spider_urls = SpiderUrlsSerializer()
    
    class Meta:
        model = Scraper
        fields = '__all__'



class ScraperSerializer(serializers.ModelSerializer):
    spiders = SpiderSerializer()

    class Meta:
        model = Scraper
        fields = '__all__'


