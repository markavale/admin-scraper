from ..models import (Scraper, ArticleSpider, ArticleThread,
                      Article, CrawlerSet, CrawlerItem, ScraperAnalysis)
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

@permission_classes([IsAdminUser])
@api_view(['POST', ])
def delete_necc_data(request):
    scrapers = Scraper.objects.all()
    article_spider = ArticleSpider.objects.all()
    article_thread = ArticleThread.objects.all()
    articles = Article.objects.all()
    [scraper.delete() for scraper in scrapers]
    [spider.delete() for spider in article_spider]
    [thread.delete() for thread in article_thread]
    [article.delete() for article in articles]
    return Response({"Message": "DELETED"})