from django.urls import path
from . views import PageViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('page-views', PageViewSet)

urlpatterns = [
    
]

urlpatterns += router.urls