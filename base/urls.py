from django.contrib import admin
from django.urls import path, include
# from django.conf import settings
# from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html')),
    path('login', TemplateView.as_view(template_name='index.html')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include("scraper.urls")),
    path('auth/', include('users.urls')),
    path('api/', include('analytics.urls')),
    path('api/', include("marketing.urls")),
    
    # path('account/', include('allauth.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += path('__debug__/', include(debug_toolbar.urls)),

    # urlpatterns += static(settings.STATIC_URL,
    #                       document_root=settings.STATIC_ROOT)
    # urlpatterns += static(settings.MEDIA_URL,
    #                       document_root=settings.MEDIA_ROOT)
