import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _


class City(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name = 'city'
        verbose_name_plural = 'cities'
