from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Mail(models.Model):
    name            = models.CharField(max_length=70)
    subject         = models.CharField(max_length=70, blank=True, null=True)
    email           = models.EmailField(max_length=70)
    message         = models.TextField(max_length=255)
    seen	    = models.BooleanField(default=False)
    timestamp       = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Rating(models.Model):
    rate            = models.FloatField()
    comment         = models.TextField(max_length=255, blank=True, null=True)
    timestamp       = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Annonymous user rated {0} stars".format(self.rate)

    



