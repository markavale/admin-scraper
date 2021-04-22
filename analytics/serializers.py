from rest_framework import serializers
from .models import PageVisit

class PageVisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = PageVisit
        fields = '__all__'
        extra_kwargs = {
            'ip': {'read_only': True}
            }

    # def save(self, *args, **kwargs):
    #     obj = PageVisit.objects.get(id=1)
    #     obj.count += 1
    #     obj.save()