from requests import request
from ..models import (Scraper, ArticleSpider, ArticleThread,
                      Article, CrawlerSet, CrawlerItem, ScraperAnalysis)
from ..serializers import (ScraperSerializer, ArticleSpiderSerializer, ArticleThreadSerializer, ArticleSerializer,
                           CrawlerSetSerializer, CrawlerItemSerializer, ScraperAnalysisSerializer)
from ..pagination import CrawlerItemPagination, ScraperPagination, ArticleSpiderPagination, ArticleThreadPagination, ArticlePagination
# from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework import viewsets, status, filters
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.utils.decorators import method_decorator
# from django.views.decorators.cache import cache_page
# from django.views.decorators.vary import vary_on_cookie
import datetime, time, json, math, statistics
from django.conf import settings
from django.db.models import Avg 

# FOR ARTICLE ERRORS
def get_article_errors(request):
    articles = CrawlerItem.objects.filter(article_status="Error")#.select_related()
    if articles.exists():
        return articles
        # serializer = CrawlerItemSerializer(articles, many=True)
        # return serializer.data
    return None

def get_article_timeout(request):
    articles = CrawlerItem.objects.filter(article_error_status="Timeout Error")#.select_related()
    if articles.exists():
        return articles
        # serializer = CrawlerItemSerializer(articles, many=True)
        # return serializer.data
    return None

def get_base_error(request):
    articles = CrawlerItem.objects.filter(article_error_status="Base Error")#.select_related()
    if articles.exists():
        return articles
        # serializer = CrawlerItemSerializer(articles, many=True)
        # return serializer.data
    return None

def get_done_articles(request):
    articles = CrawlerItem.objects.filter(article_status="Done")#.select_related()
    if articles.exists():
        return articles
        # serializer = CrawlerItemSerializer(articles, many=True)
        # return serializer.data
    return None

def get_http_503(request):
    articles = CrawlerItem.objects.filter(article_error_status="HTTP Error 403")#.select_related()
    if articles.exists():
        return articles
        # serializer = CrawlerItemSerializer(articles, many=True)
        # return serializer.data
    return None

def get_dns_error(request):
    articles = CrawlerItem.objects.filter(article_error_status="DNS Error")
    if articles.exists():
        return articles
    return None

def get_no_content(request):
    articles = CrawlerItem.objects.filter(article_error_status="No content")#.select_related()
    if articles.exists():
        return articles
        # serializer = CrawlerItemSerializer(articles, many=True)
        # return serializer.data
    return None

def get_article_fqdn_none(request):
    articles = CrawlerItem.objects.filter(fqdn=None)
    if articles.exists():
        return articles
    return None


# FOR ARTICLE DOWNLOAD LATENCY
def get_download_latency_not_none(request):
    articles = CrawlerItem.objects.filter(article_status = "Done")
    if articles.exists():
        return articles
    return None