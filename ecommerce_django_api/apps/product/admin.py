from django.contrib import admin
from .models import Product, Brand, Category


@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = (
        "uuid",
        "name",
        "description",
        "brand",
        "category",
        "created",
        "modified",
    )
    list_display_links = ("uuid", "name", "brand", "category")


@admin.register(Brand)
class BrandModelAdmin(admin.ModelAdmin):
    list_display = ("uuid", "name", "created", "modified")
    list_display_links = ("uuid", "name")


@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ("uuid", "name", "created", "modified")
    list_display_links = ("uuid", "name")
