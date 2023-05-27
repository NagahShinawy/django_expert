from rest_framework.pagination import PageNumberPagination


class CategoryPagination(PageNumberPagination):
    page_size = 3


class BrandPagination(PageNumberPagination):
    page_size = 2
