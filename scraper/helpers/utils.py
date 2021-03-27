from ..models import (Scraper, ArticleSpider, ArticleThread,
                      Article, CrawlerSet, CrawlerItem, ScraperAnalysis)
from ..serializers import (ScraperSerializer, ArticleSpiderSerializer, ArticleThreadSerializer, ArticleSerializer,
                           CrawlerSetSerializer, CrawlerItemSerializer, ScraperAnalysisSerializer)
'''
    @ SCRAPER ANALYSIS FUNCTION HELPERS
'''
# GET or CREATE: scraper analysis function for creating or getting the first object
def get_scraper_analysis(request):
    scraper_analysis = ScraperAnalysis.objects.all()
    if scraper_analysis.exists():
        return scraper_analysis[0]
    else:
        obj = ScraperAnalysis.objects.create()
        return obj


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
