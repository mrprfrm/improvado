import uuid

from django.db import models


class Series(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    source = models.CharField(max_length=255)
    temperature = models.CharField(max_length=8)
    timestamp = models.DateTimeField(auto_created=True)

    city = models.ForeignKey(
        'cities.City',
        on_delete=models.CASCADE,
        related_name='series'
    )

    class Meta:
        verbose_name = 'weather series'
        verbose_name_plural = 'weather series'
