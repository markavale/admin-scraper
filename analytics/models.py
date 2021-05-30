from django.db import models
# from django.utils import timezone
from datetime import datetime, timedelta

class PageVisit(models.Model):
    count = models.IntegerField(default=1)
    ip = models.GenericIPAddressField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.ip:
            return self.ip
        return "View"

class PageViewsAnalytics(models.Model): 
    viewers = models.ManyToManyField(PageVisit)

    class Meta:
        verbose_name_plural = "Page Views Analytics"

    def __str__(self):
        return "Page Analytics"

    def get_total_views(self):
        page_view = 0
        for views in self.viewers.all():
            page_view += views.count
        return page_view

    def get_avg_month(self):
        this_month = (datetime.now() - timedelta(days=30)).timestamp()
        views_this_month = 0
        for viewer in self.viewers.all():
            if (viewer.timestamp).timestamp() >= this_month:
                views_this_month += 1
        # views_this_month = self.viewers.filter(timestamp__lte=this_month)
        return views_this_month 

# from analytics.models import PageVisit, PageViewsAnalytics
# views = PageViewsAnalytics.objects.all()
# page = PageVisit.objects.all()
