from rest_framework import viewsets
from .models import Category, Brand, Product
from .serializers import CategorySerializer, ProductSerializer, BrandSerializer
from .pagination import CategoryPagination, BrandPagination, PageNumberPagination


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    # Custom pagination, override default Pagination comes from setting.py
    pagination_class = CategoryPagination


class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    pagination_class = BrandPagination


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = PageNumberPagination
