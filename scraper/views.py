from django.shortcuts import render
from . models import Scraper, Spider, SpiderUrls
from . serializers import SpiderUrlsSerializer, SpiderSerializer, ScraperSerializer

from django.http.response import Http404
from django.shortcuts import get_object_or_404
from django.utils import timezone
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework import  viewsets, status
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, ListCreateAPIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist


@permission_classes([AllowAny])
@api_view(['POST', ])
def scraper(request):
    data = {}
    parsed_url, created = Spider.objects.get_or_create()
    return Response()