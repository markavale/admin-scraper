from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . views import (CrawlerSetViewset, CrawlerItemviewset, ScraperViewset, scraper_logic_process, delete_necc_data,
    ArticleViewset, ArticleSpiderViewset, ArticleThreadViewset, optimize_log_file, scrapers_analysis, ScraperAnalysisViewset
)
router = DefaultRouter()

router.register('scraper-analysis', ScraperAnalysisViewset, basename='ScraperAnalysisViewset')
router.register('scrapers', ScraperViewset, basename='ScraperViewset')
router.register('article-spiders', ArticleSpiderViewset, basename='ArticleSpiderViewset')
router.register('article-threads', ArticleThreadViewset, basename='ArticleThreadViewset')
router.register('articles', ArticleViewset, basename='ArticleViewset')

router.register('crawler-sets', CrawlerSetViewset, basename='CrawlerSet')
router.register('crawler-items', CrawlerItemviewset, basename='CrawlerItemviewset')

urlpatterns = [
    path('', include(router.urls)),
    path('process-scraper/', scraper_logic_process, name='process-scraper'),
    path('scraper-analysis1/', scrapers_analysis, name='scraper-analysis'),
    path('delete/', delete_necc_data, name='delete'),
    path('check-log/', optimize_log_file, name='check-log')
]

urlpatterns += router.urls