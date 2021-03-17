from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . views import ScraperViewset

router = DefaultRouter()
router.register('scrapers', ScraperViewset)

urlpatterns = [
    path('', include(router.urls)),
]