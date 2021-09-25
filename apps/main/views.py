from django.shortcuts import render
from rest_framework import generics, viewsets

from apps.main.models import Image
from apps.main.serializers import ImageSerializer
from apps.main.tools import ImagePageNumberPagination


class ImageViewSet(viewsets.ModelViewSet):

    queryset = Image.objects.all().order_by('-created_at')
    serializer_class = ImageSerializer
    pagination_class = ImagePageNumberPagination
