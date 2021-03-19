from . models import (Scraper, ArticleSpider, SpiderCrawler, Crawler, CrawlerSet, CrawlerItem)
from . serializers import (SpiderCrawlerSerializer, ArticleSpiderSerializer, CrawlerSerializer, ScraperSerializer,
                    CrawlerSetSerializer, CrawlerItemSerialier)
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
from rest_framework.viewsets import ModelViewSet
import datetime
# from . models import Scraper
# from . serializers import ScraperSerializer

@permission_classes([IsAdminUser, IsAuthenticated,])
@api_view(['POST', ])
def main_scraper(request):
    data = {}
    parsed_url, created = SpiderCrawler.objects.get_or_create()
    return Response()

class ScraperViewset(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing the accounts
    associated with the user.
    """

    def perform_create(self, serializer):

        serializer.save(user=self.request.user)

    queryset = Scraper.objects.all()
    serializer_class = ScraperSerializer
    permission_classes = [IsAdminUser]

class CrawlerSetViewset(viewsets.ModelViewSet):
    # queryset = Order.objects.all()
    serializer_class = CrawlerSetSerializer
    lookup_field = 'id'

    def get_queryset(self):
        return CrawlerSet.objects.filter(user=self.request.user)

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def get_permissions(self):
    # """
    # Instantiates and returns the list of permissions that this view requires.
    # """
        if self.action == 'list':
            permission_classes = [IsAuthenticated]
        elif self.action == 'retrieve':
            permission_classes = [IsAuthenticated] # AllowAny
        elif self.action == 'create':
            permission_classes = [IsAdminUser] # AllowAny
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]

@permission_classes([IsAdminUser])
@api_view(['POST', ])
def add_item_crawler(request):
    date_now = datetime.datetime.now()
    saved_crawler_item = []
    data = {}
    # LOOP: save all request data to database
    for data in request.data:
        item_serializer = CrawlerItemSerializer(data=data)
        if item_serializer.is_valid():
            item_serializer.save()
            # append all saved data to list
            saved_crawler_item.append(item_serializer)
    # PASS: instantiate to a new variable
    items = saved_crawler_item
    # RETRIEVE: Get the filtered crawler set
    crawler_qs = CrawlerSet.objects.get_or_create(user= request.user, timestamp=date_now, is_finished=False)
    if crawler_qs.exists():
        crawler = crawler_qs[0]
        # TODO: check if _id already exists in database
        # If exists drop it. Otherwise, add it.
        for item in items:
            crawler.add(item)
        data['message'] = "{} item(s) successfully saved in database.".format(len(items))
    return Response(data)

@permission_classes([IsAdminUser])
@api_view(['POST', ])
def add_item_crawlers(request):
    data = {}
    cr = get_object_or_404(Item, slug=slug)

    #create order item
    article_spider, created = ArticleSpider.objects.get_or_create(user = request.user, 
        is_finished=False)
    # order_item.save()
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    # check if user has active order
    if order_qs.exists():
        order = order_qs[0] # get latest order
        # check if item already exist in cart
        if order.items.filter(item__slug=item.slug).exists():
            data['message'] = f'{item.title} was already added to your cart.'
            data['type'] = 'info'
            data['color'] = 'blue'
            print(f'{item.title} was already added to your cart.')
            return Response(data)
        else:
            order.items.add(order_item)
            data['message'] = f'{item.title} was added to your cart.'
            data['type'] = 'success'
            data['color'] = 'green'
            print(f'{item.title} was added to your cart.')
            return Response(data)
    else:
        # when user doesn't have active order
        # create new order
        date_now = timezone.now()
        order = Order.objects.create(user= request.user, start_date=date_now)
        order.items.add(order_item)
        data['message'] = f"{item.title} was added to your cart."
        data['type'] = 'success'
        print(f'{item.title} was added to your cart.')
        return Response(data)