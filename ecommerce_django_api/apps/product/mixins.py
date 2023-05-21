import uuid
from django.db import models


class NameModelMixin(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        abstract = True


class UUIDModelMixin(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class CreatedModelMixin(models.Model):
    """
    created at field mixin
    """

    created = models.DateTimeField(
        auto_now_add=True
    )  # , verbose_name="created datetime"

    class Meta:
        abstract = True


class ModifiedModelMixin(models.Model):
    """
    modified field mixin
    """

    modified = models.DateTimeField(
        auto_now=True, verbose_name="last modified datetime"
    )

    class Meta:
        abstract = True
