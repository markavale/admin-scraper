from . models import (Scraper, ArticleSpider, ArticleThread,
                      Article, CrawlerSet, CrawlerItem)
from . serializers import (ScraperSerializer, ArticleSpiderSerializer, ArticleThreadSerializer, ArticleSerializer,
                           CrawlerSetSerializer, CrawlerItemSerializer)
from django.http.response import Http404
from django.shortcuts import get_object_or_404
from django.utils import timezone
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework import viewsets, status, filters
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, ListCreateAPIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.viewsets import ModelViewSet
from .pagination import CrawlerItemPagination, ScraperPagination, ArticleSpiderPagination, ArticleThreadPagination, ArticlePagination
# from django_filters.rest_framework import DjangoFilterBackend
import datetime, time, json, math, statistics


'''
    CBVs FOR SCRAPER, ARTICLE SPIDER, ARTICLE THREAD, ARTICLE
    MAIN OBJECT => SCRAPER
        * CHILDERN OBJECTS *
            ARTICLE SPIDER => MANY TO MANY
                ARTICLE THREAD => MANY TO MANY
                    ARTICLE
'''
# CBV SCRAPER


class ScraperViewset(viewsets.ModelViewSet):
    pagination_class = ScraperPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    # filter_backends = [DjangoFilterBackend,
    #                    filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['is_finished']
    search_fields = ['user', 'workers']
    ordering = ['user', 'time_finished']
    serializer_class = ScraperSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        return Scraper.objects.all().order_by('-timestamp')

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

# CBV ARTICLE SPIDER


class ArticleSpiderViewset(viewsets.ModelViewSet):
    serializer_class = ArticleSpiderSerializer
    pagination_class = ArticleSpiderPagination
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['in_use']
    lookup_field = 'id'

    def get_queryset(self):
        return ArticleSpider.objects.all()

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

# CBV ARTICLE THREAD


class ArticleThreadViewset(viewsets.ModelViewSet):
    serializer_class = ArticleThreadSerializer
    pagination_class = ArticleThreadPagination
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['in_use']
    lookup_field = 'id'

    def get_queryset(self):
        return ArticleThread.objects.all()

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

# CBV ARTICLE


class ArticleViewset(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    pagination_class = ArticlePagination
    filter_backends = [filters.SearchFilter]
    # filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    # filterset_fields = ['in_use']
    search_fields = ['article_id', 'url']
    lookup_field = 'id'

    def get_queryset(self):
        return Article.objects.all()

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
@api_view(['POST', ])
def delete_necc_data(request):
    scrapers = Scraper.objects.all()
    article_spider = ArticleSpider.objects.all()
    article_thread = ArticleThread.objects.all()
    articles = Article.objects.all()
    [scraper.delete() for scraper in scrapers]
    [spider.delete() for spider in article_spider]
    [thread.delete() for thread in article_thread]
    [article.delete() for article in articles]
    return Response({"Message": "DELETED"})

# MAIN LOGIC FUNCTION FOR SAVING AND ADDING OBJECTS IN SCRAPER

@permission_classes([IsAdminUser])
@api_view(['POST', ])
def scraper_logic_process(request):
    # TESTING AREA DATA
    t1 = time.perf_counter()
    # f = open('test_data.json')
    # data = json.load(f)
    # TESTONG AREA END

    data = request.data

    # GET: get crawler set is_finished = False
    crawler_set = get_crawler_crawler_set(request)
    # GET: get scraper obj is_finished = False
    scraper = scraper_obj_not_finish(request)

    # INITIALIZE split data of fime finished => hour, minute, second
    hour, minute, second = data.get('time_finished').split(':')
    # hour, minute, second = request.data.get('time_finished').split(':')

    # INITIALIZE CHUNKED SPIDERS
    spiders = data.get('spiders')

    try:
        # LOOP: ADD & SAVE all ARTICLES to its respective THREAD, then add THREADS to its respective SPIDER
        # => when finish or succesfull update in_use and is_finished = True
        for spider in spiders:
            # GET or CREATE: get the current not in use spider obj
            spider_obj = get_article_spider_not_in_use(request)
            print("----------------- : SPIDER INSTANCE START HERE")
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

        # UPDATE: update crawler set in_use into True
        crawler_set.is_finished = True
        crawler_set.save()
        print("ALL DONE!")
        print(round(time.perf_counter() - t1, 2))
    except Exception as e:
        print(e)

    # END OF LOGIC :)
    return Response({"message": "Succesfully created Scraper Object"})


'''
    ALL function helpers for SCRAPER OBJECT
    SCRAPER             => get or create SCRAPER object
    ARTICLE SPIDER      => get or create ARTICLE SPIDER object
    ARTICLE THREAD      => get or create ARTICLE THREAD object
    ARTICLE             => save article
'''
# FUNCTION for returning SCRAPER not finish. If exists retrieve, else generate new SCRAPER object is_finished = False.


def scraper_obj_not_finish(request):
    try:
        crawler_set = get_crawler_crawler_set(request)
        scraper_obj = Scraper.objects.filter(
            user=request.user, is_finished=False)
        if scraper_obj.exists():
            scraper = scraper_obj[0]
        else:
            scraper = Scraper.objects.create(
                user=request.user, is_finished=False)
    except Exception as e:
        print(e)

    return scraper

# FUNCTION for returning article spider not in use. If exists retrive, else generate new ARTICLE SPIDER object in_use = False.


def get_article_spider_not_in_use(request):
    spider_obj = ArticleSpider.objects.filter(user=request.user, in_use=False)
    if spider_obj.exists():
        spider = spider_obj[0]
    else:
        spider = ArticleSpider.objects.create(user=request.user, in_use=False)
    return spider

# FUNCTION for returning for not in use article threads. If exists retrieve, else generate new THREAD object in_use = False.


def get_article_thread_not_in_use(request):
    thread_obj = ArticleThread.objects.filter(user=request.user, in_use=False)
    if thread_obj.exists():
        thread = thread_obj[0]
    else:
        thread = ArticleThread.objects.create(user=request.user, in_use=False)
    return thread

# FUNCTION for returning not in use artilces


def get_articles_not_in_use(request):
    articles = Article.objects.filter(in_use=False)
    if articles.exists():
        return articles
    else:
        return Response({"Error": "No articles available"})

# FUNCTION for saving articles


def add_article(request, articles):
    for article in articles:
        serializer = ArticleSerializer(data=article)
        if serializer.is_valid():
            serializer.save()
            print("article saved!!")
    article_objs = Article.objects.filter(in_use=False)
    return


'''
    ALL function helpers for CRAWLER SET OBJECT
    CRAWLER SET         => get or create CRAWLER SET object

'''
# FUNCTION for returning crawler set not finish. If exists retrieve, else generate new CRAWLER SET is_finished = False.


def get_crawler_crawler_set(request):
    crawler_set = CrawlerSet.objects.filter(
        user=request.user, is_finished=False)
    if crawler_set.exists():
        crawler_obj = crawler_set[0]
    else:
        crawler_obj = CrawlerSet.objects.create(
            user=request.user, is_finished=False)
    return crawler_obj

# FUNCTION for saving and adding crawler item.


def save_crawler_item_to_crawler_set(self, request, crawler_obj, is_exist):
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
        # f = open('test_article_items.json')
        # test_data = json.load(f)
        resp_data = {}
        # data = test_data
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
        crawler_items = save_crawler_item_to_crawler_set(self,
                                                         request, crawler_obj, False)
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
    missed_article_list     = list(map(lambda scraper:abs(scraper.data - scraper.crawler_set.get_total_articles()) , scrapers))
    
    data['total_data']                      = sum(data_list)
    data['total_articles']                  = len(articles)
    data['average_download_latency']        = round(statistics.mean(download_latency_list), 2)

    data['successful_parsed_articles']      = sum(parsed_article_list)
    data['unsuccessful_parse_articles']     = sum(error_list)
    data['missed_articles']                 = sum(missed_article_list)
    
    data['total_scraping_rounds']           = len(scrapers)
    
    

    return Response(data, status=status.HTTP_200_OK)


def get_scrapers(request):
    try:
        scrapers    = Scraper.objects.filter(is_finished=True)
        return scrapers
    except:
        return Response({"data": "No data available"})

def get_crawler_sets(request):
    try:
        article_data    = CrawlerSet.objects.filter(is_finished=True)
        return article_data
    except:
        return Response({"data": "No data available"})

def get_articles(request):
    try:
        articles    = Article.objects.filter(in_use=True)
        return articles
    except:
        return Response({"data": "No articles available"})