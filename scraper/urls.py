from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . views import CrawlerSetViewset, CrawlerItemiewset, ScraperViewset, scraper_logic_view, delete_necc_data

router = DefaultRouter()
router.register('scrapers', ScraperViewset)
router.register('crawler-sets', CrawlerSetViewset, basename='CrawlerSet')
router.register('crawler-items', CrawlerItemiewset, basename='CrawlerItemiewset')

urlpatterns = [
    path('', include(router.urls)),
    path('test-scraper/', scraper_logic_view, name='test-scraper'),
    path('delete/', delete_necc_data, name='delete')
]