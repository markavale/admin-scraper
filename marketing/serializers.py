from rest_framework import serializers
from . models import Mail, Rating


class MailSerailizer(serializers.ModelSerializer):
    class Meta:
        model = Mail
        fields = '__all__'


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'