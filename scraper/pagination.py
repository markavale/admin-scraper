from rest_framework.pagination import PageNumberPagination


class CrawlerItemPagination(PageNumberPagination):
    page_size = 15
    page_size_query_param = 'page_size'
    max_page_size = 10000


class ScraperPagination(PageNumberPagination):
    page_size = 1
    pagee_size_query_param = 'page_size'
    max_page_size = 10000