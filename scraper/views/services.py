from ..models import (Scraper, ArticleSpider, ArticleThread,
                      Article, CrawlerSet, CrawlerItem, ScraperAnalysis)
from ..serializers import (ScraperSerializer, ArticleSpiderSerializer, ArticleThreadSerializer, ArticleSerializer,
                           CrawlerSetSerializer, CrawlerItemSerializer, ScraperAnalysisSerializer)
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework import viewsets, status, filters
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, ListCreateAPIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from ..pagination import CrawlerItemPagination, ScraperPagination, ArticleSpiderPagination, ArticleThreadPagination, ArticlePagination
# from django_filters.rest_framework import DjangoFilterBackend
import datetime, time, json, math, statistics
from .selectors import (get_scraper_analysis, scraper_obj_not_finish, get_article_spider_not_in_use, get_article_thread_not_in_use,
            get_articles_not_in_use, add_article, get_crawler_crawler_set
)
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.utils.decorators import method_decorator
# from django.views.decorators.cache import cache_page
# from django.views.decorators.vary import vary_on_cookie
from django.db import transaction
from .selectors import (get_scrapers, get_crawler_sets, get_articles)

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)

is_testing = settings.TESTING

# @cache_page(CACHE_TTL)
@permission_classes([IsAdminUser])
@api_view(['GET'])
def dashboard(request):

    scraper_by_date = Scraper.objects.filter()
    march_24 = Scraper.objects.filter(timestamp__year='2021', timestamp__month='03', timestamp__day='24')
    march_25 = Scraper.objects.filter(timestamp__year='2021', timestamp__month='03', timestamp__day='25')
    march_26 = Scraper.objects.filter(timestamp__year='2021', timestamp__month='03', timestamp__day='26')
    march_27 = Scraper.objects.filter(timestamp__year='2021', timestamp__month='03', timestamp__day='27')
    march_28 = Scraper.objects.filter(timestamp__year='2021', timestamp__month='03', timestamp__day='28')
    march_29 = Scraper.objects.filter(timestamp__year='2021', timestamp__month='03', timestamp__day='29')
    # print(len(dates))
    # samples = Scraper.objects.filter(timestamp__gte=datetime.date(2021, 3, 24),
    #                             sampledate__lte=datetime.date(2021, 3, 25))    
    data_march_24 = list(map(lambda scraper: scraper.crawler_set.get_total_parsed_article(), march_24))
    data_march_25 = list(map(lambda scraper: scraper.crawler_set.get_total_parsed_article(), march_25))
    data_march_26 = list(map(lambda scraper: scraper.crawler_set.get_total_parsed_article(), march_26))
    data_march_27 = list(map(lambda scraper: scraper.crawler_set.get_total_parsed_article(), march_27))
    data_march_28 = list(map(lambda scraper: scraper.crawler_set.get_total_parsed_article(), march_28))
    data_march_29 = list(map(lambda scraper: scraper.crawler_set.get_total_parsed_article(), march_29))

    dates = []
    dates.append(len(march_24))
    dates.append(len(march_25))
    dates.append(len(march_26))
    dates.append(len(march_27))
    dates.append(len(march_28))
    dates.append(len(march_29))
    data = {}
    results = []

    results.append(dict({
        "total_data": sum(list(map(lambda scraper: scraper.crawler_set.get_total_articles(), march_24))),
        "success":sum(list(map(lambda scraper: scraper.crawler_set.get_total_parsed_article(), march_24))),
        "error": sum(list(map(lambda scraper: scraper.crawler_set.get_total_error(), march_24))),
        "skip": sum(list(map(lambda scraper: scraper.crawler_set.get_total_skip_error(), march_24))),
        "date": list(map(lambda scraper:scraper.timestamp, march_24))[0]
    }))
    
    results.append(dict({
        "total_data": sum(list(map(lambda scraper: scraper.crawler_set.get_total_articles(), march_25))),
        "success":sum(list(map(lambda scraper: scraper.crawler_set.get_total_parsed_article(), march_25))),
        "error": sum(list(map(lambda scraper: scraper.crawler_set.get_total_error(), march_25))),
        "skip": sum(list(map(lambda scraper: scraper.crawler_set.get_total_skip_error(), march_25))),
        "date": list(map(lambda scraper:scraper.timestamp, march_25))[0]
    }))

    results.append(dict({
        "total_data": sum(list(map(lambda scraper: scraper.crawler_set.get_total_articles(), march_26))),
        "success":sum(list(map(lambda scraper: scraper.crawler_set.get_total_parsed_article(), march_26))),
        "error": sum(list(map(lambda scraper: scraper.crawler_set.get_total_error(), march_26))),
        "skip": sum(list(map(lambda scraper: scraper.crawler_set.get_total_skip_error(), march_26))),
        "date": list(map(lambda scraper:scraper.timestamp, march_26))[0]
    }))
    
    results.append(dict({
        "total_data": sum(list(map(lambda scraper: scraper.crawler_set.get_total_articles(), march_27))),
        "success":sum(list(map(lambda scraper: scraper.crawler_set.get_total_parsed_article(), march_27))),
        "error": sum(list(map(lambda scraper: scraper.crawler_set.get_total_error(), march_27))),
        "skip": sum(list(map(lambda scraper: scraper.crawler_set.get_total_skip_error(), march_27))),
        "date": list(map(lambda scraper:scraper.timestamp, march_27))[0]
    }))

    results.append(dict({
        "total_data": sum(list(map(lambda scraper: scraper.crawler_set.get_total_articles(), march_28))),
        "success":sum(list(map(lambda scraper: scraper.crawler_set.get_total_parsed_article(), march_28))),
        "error": sum(list(map(lambda scraper: scraper.crawler_set.get_total_error(), march_28))),
        "skip": sum(list(map(lambda scraper: scraper.crawler_set.get_total_skip_error(), march_28))),
        "date": list(map(lambda scraper:scraper.timestamp, march_28))[0]
    }))

    results.append(dict({
        "total_data": sum(list(map(lambda scraper: scraper.crawler_set.get_total_articles(), march_29))),
        "success":sum(list(map(lambda scraper: scraper.crawler_set.get_total_parsed_article(), march_29))),
        "error": sum(list(map(lambda scraper: scraper.crawler_set.get_total_error(), march_29))),
        "skip": sum(list(map(lambda scraper: scraper.crawler_set.get_total_skip_error(), march_29))),
        "date": list(map(lambda scraper:scraper.timestamp, march_29))[0]
    }))
    data['results'] = results
    data['total_data'] = sum(dates)
    
    return Response(data)

# MAIN LOGIC FUNCTION FOR SAVING AND ADDING OBJECTS IN SCRAPER
@transaction.atomic
@permission_classes([IsAdminUser])
@api_view(['POST', ])
def scraper_logic_process(request):
    t1 = time.perf_counter()
    # TESTING AREA DATA
    if is_testing:
        f = open('test_data.json')
        data = json.load(f)
    # PRODUCTION DATA
    else:
        data = request.data

    #GET: get scraper analysis object
    scraper_analysis = get_scraper_analysis(request)

    # GET: get crawler set is_finished = False
    crawler_set = get_crawler_crawler_set(request)

    # GET: get scraper obj is_finished = False
    scraper = scraper_obj_not_finish(request)

    # INITIALIZE split data of fime finished => hour, minute, second
    hour, minute, second = data.get('time_finished').split(':')

    # INITIALIZE CHUNKED SPIDERS
    spiders = data.get('spiders')

    try:
        # LOOP: ADD & SAVE all ARTICLES to its respective THREAD, then add THREADS to its respective SPIDER
        # => when finish or succesfull update in_use and is_finished = True
        for spider in spiders:
            # GET or CREATE: get the current not in use spider obj
            spider_obj = get_article_spider_not_in_use(request)
            print("----------------- : SPIDER START")
            # ADD & SAVE: save all article items and add to thread object || LOOP: for loop of all threads for each spider.
            for thread_obj in spider:
                thread = get_article_thread_not_in_use(request)
                # LOOP: ARTICLE(S) PER THREAD
                for obj in thread_obj:
                    print("")
                    print(thread_obj[obj])
                    # SAVE ARTICLE and add to its respective THREAD
                    add_article(request, thread_obj[obj])
                    print("")

                    # GET: Assign all articles not in use
                    articles = get_articles_not_in_use(request)

                    # LOOP: Add all recent saved articles to current thread.
                    for article in articles:
                        print("article added to its respective THREAD")
                        thread.articles.add(article)
                        article.in_use = True
                        article.save()

                    # ADD: add current thread to existing not in_use spider object
                    spider_obj.thread_crawlers.add(thread)
                    thread.in_use = True
                    thread.save()
                    print("THREAD added to its respective SPIDER")
                    # END OF THREAD

                # ADD: add current spider to main parent => SCRAPER OBJ with field of is_finished=False
                print("SPIDER added to its respective SCRAPER")
                scraper.spiders.add(spider_obj)
            # UPDATE: patch existing spider in_use to True => meaning its already added to main parent => SCRAPER
            spider_obj.in_use = True
            spider_obj.save()

        # End of LOOP for SPIDER
        print("END of loop for spiders")
    except Exception as e:
        print("errors in spider")
        print("Process terminated by scrapy")
        print(e)
        scraper.terminated_process = True

    # END OF LOOP | SAVE: instansiate all other required data.
    try:
        scraper.data = data.get('data')
        scraper.workers = data.get('workers')
        scraper.crawler_set = crawler_set
        scraper.info_log = data.get('info_log')
        scraper.error_log = data.get('error_log')
        scraper.time_finished = datetime.time(
            int(hour), int(minute), int(second))
        scraper.is_finished = True
        scraper.save()
        
        # ADD: add scraper object to scraper analysis object
        scraper_analysis.scrapers.add(scraper)

        # UPDATE: update crawler set in_use into True
        crawler_set.is_finished = True
        crawler_set.save()
        print("ALL DONE!")
        print(round(time.perf_counter() - t1, 2))
    except Exception as e:
        print("Error occur when saving scraper data")
        print(e)

    # END OF LOGIC :)
    return Response({"message": "Succesfully created Scraper Object"})



class CrawlerSetViewset(viewsets.ModelViewSet):
    serializer_class = CrawlerSetSerializer
    lookup_field = 'id'

    def get_queryset(self):
        return CrawlerSet.objects.all().order_by('-timestamp')

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def get_permissions(self):
        # """
        # Instantiates and returns the list of permissions that this view requires.
        # """
        if self.action == 'list':
            permission_classes = [IsAuthenticated]
        elif self.action == 'retrieve':
            permission_classes = [IsAuthenticated]  # AllowAny
        elif self.action == 'create':
            permission_classes = [IsAdminUser]  # AllowAny
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]

class CrawlerItemviewset(viewsets.ModelViewSet):
    serializer_class = CrawlerItemSerializer
    pagination_class = CrawlerItemPagination
    # filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filter_backends = [filters.SearchFilter]
    search_fields = ['article_id', 'article_error_status', 'article_url']
    lookup_field = 'id'

    def get_queryset(self):
        return CrawlerItem.objects.all().order_by('-timestamp')

    def create(self, request, *args, **kwargs):
        resp_data = {}
        if is_testing:
            f = open('test_article_items.json')
            data = json.load(f)
        else:
            data = request.data
        
        for data in data:
            print("--------------------- crawler set | ITEM")
            item_serializer = self.serializer_class(data=data)
            if item_serializer.is_valid():  
                item_serializer.save()
                print("SAVED")
        # # TODO: check if _id already exists in database
        # # If exists drop it. Otherwise, add it.
        # GET / CHECK crawler set with is_finished = False
        crawler_obj = get_crawler_crawler_set(request)
        crawler_items = save_crawler_item_to_crawler_set(request, crawler_obj, False)
        resp_data['message'] = "{} article(s) successfully added to your spiders.".format(
            len(crawler_items))
        return Response(resp_data, status=status.HTTP_201_CREATED)

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def get_permissions(self):
        # """
        # Instantiates and returns the list of permissions that this view requires.
        # """
        if self.action == 'list':
            permission_classes = [IsAuthenticated]
        elif self.action == 'retrieve':
            permission_classes = [IsAuthenticated]  # AllowAny
        elif self.action == 'create':
            permission_classes = [IsAdminUser]  # AllowAny
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]

@permission_classes([IsAdminUser])
@api_view(['GET', ])
def optimize_log_file(request):
    scrapers = Scraper.objects.all()
    data = {}
    items = []
    
    for scraper in scrapers:
        # print(len(scraper.info_log))
        # print(scraper.info_log[:4])

        divisible_n = math.ceil(len(scraper.info_log) / 4)
        chunk_info = [scraper.info_log[i:i + divisible_n]
                    for i in range(0, len(scraper.info_log), divisible_n)]
        chunked_join_str = ''.join(chunk_info[::3])
        # div_n = len(scraper.info_log) // 3
        items.append(
            {"id": scraper.id ,"divisible_n": divisible_n, "total length before": len(scraper.info_log), "total length after": len(chunked_join_str),"before": scraper.info_log, "after": chunked_join_str}
        )
    data['items'] = items
    return Response(data)

'''
    DASHBOARD RETURN JSON OBJECTS
'''
@permission_classes(['IsAdminUser'])
@api_view(['GET', ])
def scrapers_analysis(request):
    data = {}
    scrapers        = get_scrapers(request)
    article_data    = get_crawler_sets(request)
    articles        = get_articles(request)

    # LOGIC for appending and computing to get the sum of all errors
    error_list = []
    [error_list.append(article.get_total_error()) for article in article_data]
    error_list              = list(map(lambda article: article.get_total_error(), article_data))
    # Same as above => another logic is by using map

    # LOGIC for appending and computing to get the average of all download latency
    download_latency_list   = list(map(lambda article: article.get_avg_dl_latency(), article_data))

    # Total data spawned by scrapy
    data_list               = list(map(lambda scraper: scraper.data, scrapers))

    # Instantiate a list of total parsed articles
    parsed_article_list     = list(map(lambda article: article.get_total_parsed_article(), article_data))

    # LOGIC for computing an absolute total number of  missed artilces or skip articles
    missed_article_list     = list(map(lambda scraper: scraper.get_total_missed_articles(), scrapers))
    

    data['total_data']                      = sum(data_list)
    data['total_articles']                  = len(articles)
    data['average_download_latency']        = round(statistics.mean(download_latency_list), 2)

    data['successful_parsed_articles']      = sum(parsed_article_list)
    data['unsuccessful_parse_articles']     = sum(error_list)
    data['missed_articles']                 = sum(missed_article_list)
    
    data['total_scraping_rounds']           = len(scrapers)
    
    return Response(data, status=status.HTTP_200_OK)


'''
    ALL function helpers for CRAWLER SET OBJECT
    CRAWLER SET         => get or create CRAWLER SET object

'''

# FUNCTION for saving and adding crawler item.


def save_crawler_item_to_crawler_set(request, crawler_obj, is_exist):
    # GET: get all crawler items with in_use = False
    crawler_items = CrawlerItem.objects.filter(in_use=False)
    if is_exist:
        for item in crawler_items:
            print(item)
            try:
                crawler_obj.crawlers.add(item)
                item.in_use = True
                item.save()
                print("{} was successfully added as item crawler".format(item))
            except Exception as e:
                print("Error")
                print(e)
    else:
        for item in crawler_items:
            try:
                crawler_obj.crawlers.add(item)
                item.in_use = True
                item.save()
                print("{} was successfully added as item crawler".format(item))
            except Exception as e:
                print("Error")
                print(e)
    return crawler_items