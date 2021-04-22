from django.contrib import admin
from . models import PageVisit, PageViewsAnalytics

class PageVisitAdmin(admin.ModelAdmin):
    list_display = ('count', 'ip', 'timestamp')


admin.site.register(PageVisit, PageVisitAdmin)
admin.site.register(PageViewsAnalytics)