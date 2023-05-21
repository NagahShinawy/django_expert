from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from .mixins import (
    NameModelMixin,
    UUIDModelMixin,
    ModifiedModelMixin,
    CreatedModelMixin,
)


class Brand(
    NameModelMixin, CreatedModelMixin, ModifiedModelMixin, UUIDModelMixin, models.Model
):
    def __str__(self):
        return self.name


class Category(
    NameModelMixin, CreatedModelMixin, ModifiedModelMixin, UUIDModelMixin, MPTTModel
):
    parent = TreeForeignKey("self", on_delete=models.PROTECT, null=True, blank=True)

    class MPTTMeta:
        order_insertion_by = ["created"]

    def __str__(self):
        return self.name


class Product(
    NameModelMixin, CreatedModelMixin, ModifiedModelMixin, UUIDModelMixin, models.Model
):
    brand = models.ForeignKey(to=Brand, on_delete=models.CASCADE)
    category = TreeForeignKey(
        "Category", null=True, blank=True, on_delete=models.SET_NULL
    )
    description = models.TextField(max_length=500)
    is_digital = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
