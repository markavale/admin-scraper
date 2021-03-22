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
from .pagination import CrawlerItemPagination, ScraperPagination
from django_filters.rest_framework import DjangoFilterBackend
import datetime

# @permission_classes([IsAdminUser, IsAuthenticated, ])
# @api_view(['POST', ])
# def main_scraper(request):
#     data = {}
#     parsed_url, created = SpiderCrawler.objects.get_or_create()
#     return Response()


class ScraperViewset(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing the accounts
    associated with the user.
    """
    pagination_class = ScraperPagination
    filter_backends = [DjangoFilterBackend,
                       filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['is_finished']
    search_fields = ['user', 'workers']
    ordering = ['user', 'time_finished']

    def perform_create(self, serializer):

        serializer.save(user=self.request.user)

    queryset = Scraper.objects.all()
    serializer_class = ScraperSerializer
    permission_classes = [IsAdminUser]


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


@permission_classes([IsAdminUser])
@api_view(['POST', ])
def scraper_logic_view(request):
    data = {'crawler_items': '',
            'data': 50,
            'error_log': ['|| Total spider/worker: 6 \n',
                          '21/03/21 - 14:04:31 - news_extractor - INFO - Spider links: 3\n',
                          '21/03/21 - 14:04:31 - news_extractor - INFO - Spider links: 3\n',
                          '21/03/21 - 14:04:31 - news_extractor - INFO - Spider links: 3\n',
                          '21/03/21 - 14:04:31 - news_extractor - INFO - Spider links: 3\n',
                          '21/03/21 - 14:04:31 - news_extractor - INFO - Spider links: 3\n',
                          '21/03/21 - 14:04:31 - news_extractor - INFO - Spider links: 3\n',
                          '21/03/21 - 14:04:31 - news_extractor - INFO - Finished scraping '
                          'in 0:00:01\n',
                          '21/03/21 - 14:05:21 - news_extractor - INFO - Total links: 50 '
                          '|| Total spider/worker: 6 \n',
                          '21/03/21 - 14:05:22 - news_extractor - INFO - Spider links: 3\n',
                          '21/03/21 - 14:05:22 - news_extractor - INFO - Spider links: 3\n',
                          '21/03/21 - 14:05:22 - news_extractor - INFO - Spider links: 3\n',
                          '21/03/21 - 14:05:22 - news_extractor - INFO - Spider links: 3\n',
                          '21/03/21 - 14:05:22 - news_extractor - INFO - Spider links: 3\n',
                          '21/03/21 - 14:05:22 - news_extractor - INFO - Spider links: 3\n',
                          '21/03/21 - 14:05:22 - news_extractor - INFO - Finished scraping '
                          'in 0:00:01\n',
                          '21/03/21 - 14:06:04 - news_extractor - INFO - Total links: 50 '
                          '|| Total spider/worker: 6 \n',
                          '21/03/21 - 14:06:05 - news_extractor - INFO - Spider links: 3\n',
                          '21/03/21 - 14:06:05 - news_extractor - INFO - Spider links: 3\n',
                          '21/03/21 - 14:06:05 - news_extractor - INFO - Spider links: 3\n',
                          '21/03/21 - 14:06:05 - news_extractor - INFO - Spider links: 3\n',
                          '21/03/21 - 14:06:05 - news_extractor - INFO - Spider links: 3\n',
                          '21/03/21 - 14:06:05 - news_extractor - INFO - Spider links: 3\n', ],
            'info_log': ['21/03/21 - 14:04:29 - news_extractor - INFO - Total links: 100 '
                         '|| Total spider/worker: 6 \n',
                         '21/03/21 - 14:04:31 - news_extractor - INFO - Spider links: 3\n',
                         '21/03/21 - 14:04:31 - news_extractor - INFO - Spider links: 3\n',
                         '21/03/21 - 14:04:31 - news_extractor - INFO - Spider links: 3\n',
                         '21/03/21 - 14:04:31 - news_extractor - INFO - Spider links: 3\n',
                         '21/03/21 - 14:04:31 - news_extractor - INFO - Spider links: 3\n',
                         '21/03/21 - 14:04:31 - news_extractor - INFO - Spider links: 3\n',
                         '21/03/21 - 14:04:31 - news_extractor - INFO - Finished scraping '
                         'in 0:00:01\n',
                         '21/03/21 - 14:05:21 - news_extractor - INFO - Total links: 50 '
                         '|| Total spider/worker: 6 \n',
                         '21/03/21 - 14:05:22 - news_extractor - INFO - Spider links: 3\n',
                         '21/03/21 - 14:05:22 - news_extractor - INFO - Spider links: 3\n',
                         '21/03/21 - 14:05:22 - news_extractor - INFO - Spider links: 3\n',
                         '21/03/21 - 14:05:22 - news_extractor - INFO - Spider links: 3\n',
                         '21/03/21 - 14:05:22 - news_extractor - INFO - Spider links: 3\n',
                         '21/03/21 - 14:05:22 - news_extractor - INFO - Spider links: 3\n',
                         '21/03/21 - 14:05:22 - news_extractor - INFO - Finished scraping '
                         'in 0:00:01\n',
                         '21/03/21 - 14:06:04 - news_extractor - INFO - Total links: 50 '
                         '|| Total spider/worker: 6 \n',
                         '21/03/21 - 14:06:05 - news_extractor - INFO - Spider links: 3\n',
                         '21/03/21 - 14:06:05 - news_extractor - INFO - Spider links: 3\n',
                         '21/03/21 - 14:06:05 - news_extractor - INFO - Spider links: 3\n',
                         '21/03/21 - 14:06:05 - news_extractor - INFO - Spider links: 3\n',
                         '21/03/21 - 14:06:05 - news_extractor - INFO - Spider links: 3\n',
                         '21/03/21 - 14:06:05 - news_extractor - INFO - Spider links: 3\n',
                         '21/03/21 - 14:06:05 - news_extractor - INFO - Finished scraping '
                         'in 0:00:01\n',
                         '21/03/21 - 14:07:03 - news_extractor - INFO - Total links: 50 '
                         '|| Total spider/worker: 6 \n',
                         '21/03/21 - 14:07:04 - news_extractor - INFO - Spider links: 3\n',
                         '21/03/21 - 14:07:04 - news_extractor - INFO - Spider links: 3\n',
                         '21/03/21 - 14:07:05 - news_extractor - INFO - Spider links: 3\n',
                         '21/03/21 - 14:07:05 - news_extractor - INFO - Spider links: 3\n',
                         '21/03/21 - 14:07:05 - news_extractor - INFO - Spider links: 3\n',
                         '21/03/21 - 14:07:05 - news_extractor - INFO - Spider links: 3\n',
                         '21/03/21 - 14:07:05 - news_extractor - INFO - Finished scraping '
                         'in 0:00:01\n',
                         '21/03/21 - 14:09:46 - news_extractor - INFO - Total links: 50 '
                         '|| Total spider/worker: 6 \n',
                         '21/03/21 - 14:09:47 - news_extractor - INFO - Spider links: 3\n',
                         '21/03/21 - 14:09:47 - news_extractor - INFO - Spider links: 3\n',
                         '21/03/21 - 14:09:47 - news_extractor - INFO - Spider links: 3\n',
                         '21/03/21 - 14:09:47 - news_extractor - INFO - Spider links: 3\n',
                         '21/03/21 - 14:09:47 - news_extractor - INFO - Spider links: 3\n',
                         '21/03/21 - 14:09:47 - news_extractor - INFO - Spider links: 3\n',
                         '21/03/21 - 14:09:47 - news_extractor - INFO - Finished scraping '
                         'in 0:00:01\n',
                         '21/03/21 - 14:10:24 - news_extractor - INFO - Total links: 50 '
                         '|| Total spider/worker: 6 \n',
                         '21/03/21 - 14:10:25 - news_extractor - INFO - Spider links: 3\n',
                         '21/03/21 - 14:10:25 - news_extractor - INFO - Spider links: 3\n',
                         '21/03/21 - 14:10:25 - news_extractor - INFO - Spider links: 3\n',
                         '21/03/21 - 14:10:25 - news_extractor - INFO - Spider links: 3\n',
                         '21/03/21 - 14:10:26 - news_extractor - INFO - Spider links: 3\n',
                         '21/03/21 - 14:10:26 - news_extractor - INFO - Spider links: 3\n',
                         '21/03/21 - 14:10:26 - news_extractor - INFO - Finished scraping '
                         'in 0:00:01\n',
                         '21/03/21 - 14:13:22 - news_extractor - INFO - Total links: 50 '
                         '|| Total spider/worker: 6 \n',
                         '21/03/21 - 14:13:23 - news_extractor - INFO - Spider links: 3\n',
                         '21/03/21 - 14:13:23 - news_extractor - INFO - Spider links: 3\n',
                         '21/03/21 - 14:13:24 - news_extractor - INFO - Spider links: 3\n',
                         '21/03/21 - 14:13:24 - news_extractor - INFO - Spider links: 3\n',
                         '21/03/21 - 14:13:24 - news_extractor - INFO - Spider links: 3\n',
                         '21/03/21 - 14:13:24 - news_extractor - INFO - Spider links: 3\n',
                         '21/03/21 - 14:13:24 - news_extractor - INFO - Finished scraping '
                         'in 0:00:01\n'],
            'is_finished': True,
            'json_log': '',
            'spiders': [[{'thread_crawlers': [{'article_id': '1231231',
                                               'url': 'http://www.nytimes.com/2021/02/25/podcasts/still-processing-best-of-the-archives-whitney-houston.html3123'},
                                              {'article_id': '1231231',
                                               'url': 'http://www.nytimes.com/2021/02/28/us/schools-reopening-philadelphia-parents.html'},
                                              {'article_id': '1231231',
                                               'url': 'http://www.nytimes.com/2021/02/25/podcasts/still-processing-best-of-the-archives-whitney-houston.html3123'}]},
                         {'thread_crawlers': [{'article_id': '1231231',
                                               'url': 'http://www.nytimes.com/2021/02/28/us/schools-reopening-philadelphia-parents.html'},
                                              {'article_id': '1231231',
                                               'url': 'http://www.nytimes.com/2021/02/25/podcasts/still-processing-best-of-the-archives-whitney-houston.html3123'},
                                              {'article_id': '1231231',
                                               'url': 'http://www.nytimes.com/2021/02/28/us/schools-reopening-philadelphia-parents.html'}]},
                         {'thread_crawlers': [{'article_id': '1231231',
                                               'url': 'http://www.nytimes.com/2021/02/25/podcasts/still-processing-best-of-the-archives-whitney-houston.html3123'},
                                              {'article_id': '1231231',
                                               'url': 'http://www.nytimes.com/2021/02/28/us/schools-reopening-philadelphia-parents.html'},
                                              {'article_id': '1231231',
                                               'url': 'http://www.nytimes.com/2021/02/25/podcasts/still-processing-best-of-the-archives-whitney-houston.html3123'}]}],
                        [{'thread_crawlers': [{'article_id': '1231231',
                                               'url': 'http://www.nytimes.com/2021/02/28/us/schools-reopening-philadelphia-parents.html'},
                                              {'article_id': '1231231',
                                               'url': 'http://www.nytimes.com/2021/02/25/podcasts/still-processing-best-of-the-archives-whitney-houston.html3123'},
                                              {'article_id': '1231231',
                                               'url': 'http://www.nytimes.com/2021/02/28/us/schools-reopening-philadelphia-parents.html'}]},
                         {'thread_crawlers': [{'article_id': '1231231',
                                               'url': 'http://www.nytimes.com/2021/02/25/podcasts/still-processing-best-of-the-archives-whitney-houston.html3123'},
                                              {'article_id': '1231231',
                                               'url': 'http://www.nytimes.com/2021/02/28/us/schools-reopening-philadelphia-parents.html'},
                                              {'article_id': '1231231',
                                               'url': 'http://www.nytimes.com/2021/02/25/podcasts/still-processing-best-of-the-archives-whitney-houston.html3123'}]},
                         {'thread_crawlers': [{'article_id': '1231231',
                                               'url': 'http://www.nytimes.com/2021/02/28/us/schools-reopening-philadelphia-parents.html'},
                                              {'article_id': '1231231',
                                               'url': 'http://www.nytimes.com/2021/02/25/podcasts/still-processing-best-of-the-archives-whitney-houston.html3123'},
                                              {'article_id': '1231231',
                                               'url': 'http://www.nytimes.com/2021/02/28/us/schools-reopening-philadelphia-parents.html'}]}],

                        [{'thread_crawlers': [{'article_id': '1231231',
                                               'url': 'http://www.nytimes.com/2021/02/25/podcasts/still-processing-best-of-the-archives-whitney-houston.html3123'},
                                              {'article_id': '1231231',
                                               'url': 'http://www.nytimes.com/2021/02/28/us/schools-reopening-philadelphia-parents.html'},
                                              {'article_id': '1231231',
                                               'url': 'http://www.nytimes.com/2021/02/25/podcasts/still-processing-best-of-the-archives-whitney-houston.html3123'}]},
                         {'thread_crawlers': [{'article_id': '1231231',
                                               'url': 'http://www.nytimes.com/2021/02/28/us/schools-reopening-philadelphia-parents.html'},
                                              {'article_id': '1231231',
                                               'url': 'http://www.nytimes.com/2021/02/25/podcasts/still-processing-best-of-the-archives-whitney-houston.html3123'},
                                              {'article_id': '1231231',
                                               'url': 'http://www.nytimes.com/2021/02/28/us/schools-reopening-philadelphia-parents.html'}]},
                         {'thread_crawlers': [{'article_id': '1231231',
                                               'url': 'http://www.nytimes.com/2021/02/25/podcasts/still-processing-best-of-the-archives-whitney-houston.html3123'},
                                              {'article_id': '1231231',
                                               'url': 'http://www.nytimes.com/2021/02/28/us/schools-reopening-philadelphia-parents.html'},
                                              {'article_id': '1231231',
                                               'url': 'http://www.nytimes.com/2021/02/25/podcasts/still-processing-best-of-the-archives-whitney-houston.html3123'}]}],
                        [{'thread_crawlers': [{'article_id': '1231231',
                                               'url': 'http://www.nytimes.com/2021/02/28/us/schools-reopening-philadelphia-parents.html'},
                                              {'article_id': '1231231',
                                               'url': 'http://www.nytimes.com/2021/02/25/podcasts/still-processing-best-of-the-archives-whitney-houston.html3123'},
                                              {'article_id': '1231231',
                                               'url': 'http://www.nytimes.com/2021/02/28/us/schools-reopening-philadelphia-parents.html'}]},
                         {'thread_crawlers': [{'article_id': '1231231',
                                               'url': 'http://www.nytimes.com/2021/02/25/podcasts/still-processing-best-of-the-archives-whitney-houston.html3123'},
                                              {'article_id': '1231231',
                                               'url': 'http://www.nytimes.com/2021/02/28/us/schools-reopening-philadelphia-parents.html'},
                                              {'article_id': '1231231',
                                               'url': 'http://www.nytimes.com/2021/02/25/podcasts/still-processing-best-of-the-archives-whitney-houston.html3123'}]},
                         {'thread_crawlers': [{'article_id': '1231231',
                                               'url': 'http://www.nytimes.com/2021/02/28/us/schools-reopening-philadelphia-parents.html'},
                                              {'article_id': '1231231',
                                               'url': 'http://www.nytimes.com/2021/02/25/podcasts/still-processing-best-of-the-archives-whitney-houston.html3123'},
                                              {'article_id': '1231231',
                                               'url': 'http://www.nytimes.com/2021/02/28/us/schools-reopening-philadelphia-parents.html'}]}],
                        [{'thread_crawlers': [{'article_id': '1231231',
                                               'url': 'http://www.nytimes.com/2021/02/25/podcasts/still-processing-best-of-the-archives-whitney-houston.html3123'},
                                              {'article_id': '1231231',
                                               'url': 'http://www.nytimes.com/2021/02/28/us/schools-reopening-philadelphia-parents.html'},
                                              {'article_id': '1231231',
                                               'url': 'http://www.nytimes.com/2021/02/25/podcasts/still-processing-best-of-the-archives-whitney-houston.html3123'}]},
                         {'thread_crawlers': [{'article_id': '1231231',
                                               'url': 'http://www.nytimes.com/2021/02/28/us/schools-reopening-philadelphia-parents.html'},
                                              {'article_id': '1231231',
                                               'url': 'http://www.nytimes.com/2021/02/25/podcasts/still-processing-best-of-the-archives-whitney-houston.html3123'},
                                              {'article_id': '1231231',
                                               'url': 'http://www.nytimes.com/2021/02/28/us/schools-reopening-philadelphia-parents.html'}]},

                         {'thread_crawlers': [{'article_id': '1231231',
                                               'url': 'http://www.nytimes.com/2021/02/25/podcasts/still-processing-best-of-the-archives-whitney-houston.html3123'},
                                              {'article_id': '1231231',
                                               'url': 'http://www.nytimes.com/2021/02/28/us/schools-reopening-philadelphia-parents.html'},
                                              {'article_id': '1231231',
                                               'url': 'http://www.nytimes.com/2021/02/25/podcasts/still-processing-best-of-the-archives-whitney-houston.html3123'}]}],
                        [{'thread_crawlers': [{'article_id': '1231231',
                                               'url': 'http://www.nytimes.com/2021/02/28/us/schools-reopening-philadelphia-parents.html'},
                                              {'article_id': '1231231',
                                               'url': 'http://www.nytimes.com/2021/02/25/podcasts/still-processing-best-of-the-archives-whitney-houston.html3123'}]},
                         {'thread_crawlers': [{'article_id': '1231231',
                                               'url': 'http://www.nytimes.com/2021/02/28/us/schools-reopening-philadelphia-parents.html'},
                                              {'article_id': '1231231',
                                               'url': 'http://www.nytimes.com/2021/02/25/podcasts/still-processing-best-of-the-archives-whitney-houston.html3123'}]},
                         {'thread_crawlers': [{'article_id': '1231231',
                                               'url': 'http://www.nytimes.com/2021/02/28/us/schools-reopening-philadelphia-parents.html'}]}]],
            'time_finished': '0:00:01',
            'workers': 6}
    crawler_set = get_crawler_crawler_set(request)  # REMOVE!!
    # scraper = get_scraper_obj(request) # REMOVEW THIS!!!!!]
    scraper = scraper_obj_not_finish(request)

    ### SAVE data to existing scraper object ###
    # scraper.data = data.get('data')
    # scraper.workers = data.get('workers')

    hour, minute, second = data.get('time_finished').split(':')
    error_log = data.get('error_log')
    infO_log = data.get('info_log')
    total_data = data.get('data')
    spiders = data.get('spiders')  # spider table
    workers = data.get('workers')
    try:

        for spider in spiders:
            spider_obj = get_article_spider_not_in_use(request)
            print("-----------------")
            # ADD & SAVE: save all article items and add to thread object || LOOP: for loop of all threads for each spider.
            for thread_obj in spider:
                thread = get_article_thread_not_in_use(request)
                # LOOP: ARTICLE(S) PER THREAD
                for obj in thread_obj:
                    print("")
                    print(thread_obj[obj])
                    add_article(request, thread_obj[obj])
                    print("")

                    # GET: Assign all articles not in use
                    articles = get_articles_not_in_use(request)

                    # LOOP: Add all recent saved articles to current thread.
                    for article in articles:
                        print("artilce added to thread")
                        thread.articles.add(article)
                        article.in_use = True
                        article.save()

                    # ADD: add current thread to existing not in_use spider object
                    print("thread added to spider")
                    spider_obj.thread_crawlers.add(thread)
                    thread.in_use = True
                    thread.save()
                    # END OF THREAD

                # ADD: add current spider to main parent : SCRAPER OBJ
                print("Spider added to scraper")
                scraper.spiders.add(spider_obj)
            # UPDATE: patch existing spider in_use to True
            spider_obj.in_use = True
            spider_obj.save()

    except Exception as e:
        print("error on spiders")
        priint(e)
    print("END of loop for spiders")

    # END OF LOOP | SAVE: when looping of each spider is done patch SCRAPER OBJECT is_finished into True. Also, add all other required data.

    try:
        # spider_data = get_article_spider_not_in_use(request)
        # spiders_dicts = ArticleSpiderSerializer(spider_data, many=True)
        # print(spiders_dicts)
        # scraper_data = {
        #     "data": data.get("data"),
        #     "workers": data.get('workers'),
        #     "info_log": data.get('info_log'),
        #     "error_log": data.get('error_log'),
        #     "spiders": spiders_dicts,
        #     "time_finished": datetime.time(int(hour), int(minute), int(second))
        #     "is_finished": True
        # }

        # scraper_serializer = ScraperSerializer(data=data)
        # if scraper_serializer.is_valid():
        #     scraper_serializer.save()
        #     print(scraper_serializer.data)

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
    except Exception as e:
        print(e)

    # END OF LOGIC :)
    print(scraper)
    return Response({"DATA": scraper})


def scraper_obj_not_finish(request):
    try:
        crawler_set = get_crawler_crawler_set(request)
        scraper_obj = Scraper.objects.filter(user=request.user, is_finished=False)
        if scraper_obj.exists():
            scraper = scraper_obj[0]
        else:
            scraper = Scraper.objects.create(user=request.user, is_finished=False)
    except Exception as e:
        print(e)

    return scraper


def get_article_spider_not_in_use(request):
    spider_obj = ArticleSpider.objects.filter(user=request.user, in_use=False)
    if spider_obj.exists():
        spider = spider_obj[0]
    else:
        spider = ArticleSpider.objects.create(user=request.user, in_use=False)
    return spider


def get_article_thread_not_in_use(request):
    thread_obj = ArticleThread.objects.filter(user=request.user, in_use=False)
    if thread_obj.exists():
        thread = thread_obj[0]
    else:
        thread = ArticleThread.objects.create(user=request.user, in_use=False)
    return thread


def get_articles_not_in_use(request):
    articles = Article.objects.filter(in_use=False)
    if articles.exists():
        return articles
    else:
        return Response({"Error": "No articles available"})


def add_article(request, articles):
    for article in articles:
        serializer = ArticleSerializer(data=article)
        if serializer.is_valid():
            serializer.save()
            print("item saved!!")
    article_objs = Article.objects.filter(in_use=False)
    return


def get_scraper_obj(request):
    scraper = Scraper.objects.filter(user=request.user, is_finished=False)
    if scraper.exists():
        scraper_obj = scraper[0]
    else:
        scraper_obj = Scraper.objects.create(
            user=request.user, is_finished=False)
    return scraper_obj


def get_crawler_crawler_set(request):
    crawler_set = CrawlerSet.objects.filter(
        user=request.user, is_finished=False)
    if crawler_set.exists():
        crawler_obj = crawler_set[0]
    else:
        crawler_obj = CrawlerSet.objects.create(
            user=request.user, is_finished=False)
    return crawler_obj


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
            permission_classes = [IsAuthenticated]  # AllowAny
        elif self.action == 'create':
            permission_classes = [IsAdminUser]  # AllowAny
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]


class CrawlerItemiewset(viewsets.ModelViewSet):
    serializer_class = CrawlerItemSerializer
    pagination_class = CrawlerItemPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['article_status', 'in_use', 'collection_name']
    search_fields = ['article_id', 'article_error_status', 'article_url']
    lookup_field = 'id'

    def get_queryset(self):
        return CrawlerItem.objects.all()

    def create(self, request, *args, **kwargs):
        test_data = [{'article_error_status': None,
                      'article_id': '123123123123',
                      'article_status': 'Done',
                      'article_url': 'http://www.nytimes.com/2021/02/28/us/schools-reopening-philadelphia-parents.html',
                      'base_error': 0,
                      'collection_name': 'global_link',
                      'dns_error': 0,
                      'download_latency': 0.4431931972503662,
                      'http_error': 0,
                      'skip_url': 0,
                      'timeout_error': 0},
                     {'article_error_status': None,
                      'article_id': '123123123123',
                      'article_status': 'Done',
                      'article_url': 'http://www.nytimes.com/2021/02/28/us/schools-reopening-philadelphia-parents.html',
                      'base_error': 0,
                      'collection_name': 'global_link',
                      'dns_error': 0,
                      'download_latency': 0.4431931972503662,
                      'http_error': 0,
                      'skip_url': 0,
                      'timeout_error': 0},
                     {'article_error_status': None,
                      'article_id': '123123123123',
                      'article_status': 'Done',
                      'article_url': 'http://www.nytimes.com/2021/02/25/podcasts/still-processing-best-of-the-archives-whitney-houston.html',
                      'base_error': 0,
                      'collection_name': 'global_link',
                      'dns_error': 0,
                      'download_latency': 0.4297006130218506,
                      'http_error': 0,
                      'skip_url': 0,
                      'timeout_error': 0},
                     {'article_error_status': None,
                      'article_id': '123123123123',
                      'article_status': 'Done',
                      'article_url': 'http://www.nytimes.com/2021/02/25/podcasts/still-processing-best-of-the-archives-whitney-houston.html',
                      'base_error': 0,
                      'collection_name': 'global_link',
                      'dns_error': 0,
                      'download_latency': 0.4297006130218506,
                      'http_error': 0,
                      'skip_url': 0,
                      'timeout_error': 0},
                     {'article_error_status': 'HTTP Error',
                      'article_id': '123123123123',
                      'article_status': 'Error',
                      'article_url': 'https://www.nytimes.com/2021/02/25/podcasts/still-processing-best-of-the-archives-whitney-houston.html3123',
                      'base_error': 0,
                      'collection_name': 'global_link',
                      'dns_error': 0,
                      'download_latency': None,
                      'http_error': 1,
                      'skip_url': 0,
                      'timeout_error': 0},
                     {'article_error_status': None,
                      'article_id': '123123123123',
                      'article_status': 'Done',
                      'article_url': 'http://www.nytimes.com/2021/02/28/us/schools-reopening-philadelphia-parents.html',
                      'base_error': 0,
                      'collection_name': 'global_link',
                      'dns_error': 0,
                      'download_latency': 0.4137439727783203,
                      'http_error': 0,
                      'skip_url': 0,
                      'timeout_error': 0},
                     {'article_error_status': None,
                      'article_id': '123123123123',
                      'article_status': 'Done',
                      'article_url': 'http://www.nytimes.com/2021/02/28/us/schools-reopening-philadelphia-parents.html',
                      'base_error': 0,
                      'collection_name': 'global_link',
                      'dns_error': 0,
                      'download_latency': 0.4137439727783203,
                      'http_error': 0,
                      'skip_url': 0,
                      'timeout_error': 0},
                     {'article_error_status': None,
                      'article_id': '123123123123',
                      'article_status': 'Done',
                      'article_url': 'http://www.nytimes.com/2021/02/28/us/schools-reopening-philadelphia-parents.html',
                      'base_error': 0,
                      'collection_name': 'global_link',
                      'dns_error': 0,
                      'download_latency': 0.42194604873657227,
                      'http_error': 0,
                      'skip_url': 0,
                      'timeout_error': 0},
                     {'article_error_status': None,
                      'article_id': '123123123123',
                      'article_status': 'Done',
                      'article_url': 'http://www.nytimes.com/2021/02/28/us/schools-reopening-philadelphia-parents.html',
                      'base_error': 0,
                      'collection_name': 'global_link',
                      'dns_error': 0,
                      'download_latency': 0.42194604873657227,
                      'http_error': 0,
                      'skip_url': 0,
                      'timeout_error': 0},
                     {'article_error_status': 'HTTP Error',
                      'article_id': '123123123123',
                      'article_status': 'Error',
                      'article_url': 'https://www.nytimes.com/2021/02/25/podcasts/still-processing-best-of-the-archives-whitney-houston.html3123',
                      'base_error': 0,
                      'collection_name': 'global_link',
                      'dns_error': 0,
                      'download_latency': None,
                      'http_error': 1,
                      'skip_url': 0,
                      'timeout_error': 0}]
        resp_data = {}
        for data in test_data:
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
