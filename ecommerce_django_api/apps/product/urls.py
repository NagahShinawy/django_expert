from django.urls import path, include
from rest_framework import routers
from .views import (
    CategoryViewSet,
    BrandViewSet,
    ProductViewSet,
)

router = routers.DefaultRouter()
router.register("categories", CategoryViewSet)
router.register("brands", BrandViewSet)
router.register("products", ProductViewSet)


urlpatterns = [
    path("api/", include(router.urls)),
]
