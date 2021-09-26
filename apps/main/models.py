import os
import uuid

from django.conf import settings
from django.db import models
from django.utils import timezone

from versatileimagefield.fields import VersatileImageField, PPOIField


class Image(models.Model):
    image = VersatileImageField('Изображение', upload_to='images/', ppoi_field='image_ppoi')
    image_ppoi = PPOIField()
    created_at = models.DateTimeField('Дата загрузки', editable=False, default=timezone.now)

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'

