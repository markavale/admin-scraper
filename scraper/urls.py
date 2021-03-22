from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . views import (CrawlerSetViewset, CrawlerItemiewset, ScraperViewset, scraper_logic_process, delete_necc_data,
    ArticleViewset, ArticleSpiderViewset, ArticleThreadViewset
)
router = DefaultRouter()

router.register('scrapers', ScraperViewset, basename='ScraperViewset')
router.register('article-spiders', ArticleSpiderViewset, basename='ArticleSpiderViewset')
router.register('article-threads', ArticleThreadViewset, basename='ArticleThreadViewset')
router.register('articles', ArticleViewset, basename='ArticleViewset')

router.register('crawler-sets', CrawlerSetViewset, basename='CrawlerSet')
router.register('crawler-items', CrawlerItemiewset, basename='CrawlerItemiewset')

urlpatterns = [
    path('', include(router.urls)),
    path('process-scraper/', scraper_logic_process, name='test-scraper'),
    path('delete/', delete_necc_data, name='delete')
]