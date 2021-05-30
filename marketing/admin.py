from django.contrib import admin
from . models import Mail, Rating

class MailAdmin(admin.ModelAdmin):
    list_display = ['name', 'subject', 'email', 'seen', 'message', 'timestamp']
    list_filter = ('timestamp', )

class RatingAdmin(admin.ModelAdmin):
    list_display = ['rate', 'comment', 'timestamp',]
    list_filter  = ('timestamp', )

admin.site.register(Mail, MailAdmin)
admin.site.register(Rating, RatingAdmin)
