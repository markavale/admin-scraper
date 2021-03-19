from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . views import ScraperViewset, CrawlerSetViewset, add_item_crawler

router = DefaultRouter()
router.register('scrapers', ScraperViewset)
router.register('crawler-sets', CrawlerSetViewset, basename='CrawlerSet')

urlpatterns = [
    path('', include(router.urls)),
    path('add-crawler-items', add_item_crawler, name='add-crawler-items'),
]