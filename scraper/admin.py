from django.contrib import admin
from . models import Scraper, Spider, SpiderUrls

admin.site.register(Scraper)
admin.site.register(Spider)
admin.site.register(SpiderUrls)