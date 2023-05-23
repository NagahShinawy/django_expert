from django.urls import path
from .views import CategoriesListAPIView, BrandListAPIView, ProductListAPIView


urlpatterns = [
    path("categories/", CategoriesListAPIView.as_view(), name="list-categories"),
    path("brands/", BrandListAPIView.as_view(), name="list-brands"),
    path("products/", ProductListAPIView.as_view(), name="list-products"),

]
