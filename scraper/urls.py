from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.services import (CrawlerSetViewset, CrawlerItemviewset, scraper_logic_process,
    optimize_log_file, scrapers_analysis,
    dashboard
)
from .views.selectors import (ScraperViewset, ArticleSpiderViewset, ArticleThreadViewset, 
                    ArticleViewset, ScraperAnalysisViewset, ScraperAnalysisAPIView, ScraperErrorAnalysisAPIView,
                    ScraperErrorViewset, top_websites_error, website_download_latency, test_view)
from .views.utils import (delete_necc_data)

router = DefaultRouter()

router.register('scraper-analysis', ScraperAnalysisViewset, basename='ScraperAnalysisViewset')
router.register('scrapers', ScraperViewset, basename='ScraperViewset')
router.register('article-spiders', ArticleSpiderViewset, basename='ArticleSpiderViewset')
router.register('article-threads', ArticleThreadViewset, basename='ArticleThreadViewset')
router.register('articles', ArticleViewset, basename='ArticleViewset')

# ERRORS
router.register('scraper-errors', ScraperErrorViewset, basename='ScraperErrorViewset')

router.register('crawler-sets', CrawlerSetViewset, basename='CrawlerSet')
router.register('crawler-items', CrawlerItemviewset, basename='CrawlerItemviewset')

urlpatterns = [ 
    # path('', include(router.urls)),
    path('process-scraper/', scraper_logic_process, name='process-scraper'),
    path('scraper-analysis-v1/', ScraperAnalysisAPIView.as_view(), name='scraper-analysis-v1'),
    path('scraper-analysis/', scrapers_analysis, name='scraper-analysis'), 
    path('delete/', delete_necc_data, name='delete'),
    path('check-log/', optimize_log_file, name='check-log'),
    path('dashboard/', dashboard, name='dashboard'),
    path('article-errors/', top_websites_error, name='article-errors'),
    path('website-latency/', website_download_latency, name='website-latency'),
    path('test-view/', test_view, name='test-view')
    # path('scraper-errors/', ScraperErrorAnalysisAPIView.as_view(), name='article-errors')
]

urlpatterns += router.urls