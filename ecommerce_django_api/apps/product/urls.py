from django.urls import path, include
from rest_framework import routers
from .views import (
    CategoriesListAPIView,
    BrandListAPIView,
    ProductListAPIView,
    CategoryViewSet,
    BrandViewSet,
    ProductViewSet,
)

router = routers.DefaultRouter()
router.register("categories/", CategoryViewSet)
router.register("brands/", BrandViewSet)
router.register("products/", ProductViewSet)


urlpatterns = [
    path("categories/", CategoriesListAPIView.as_view(), name="list-categories"),
    path("brands/", BrandListAPIView.as_view(), name="list-brands"),
    path("products/", ProductListAPIView.as_view(), name="list-products"),
    path("api/", include(router.urls)),
]
