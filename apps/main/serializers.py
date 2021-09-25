from rest_framework import serializers

from .models import Image
from versatileimagefield.serializers import VersatileImageFieldSerializer


class ImageSerializer(serializers.ModelSerializer):
    image = VersatileImageFieldSerializer(sizes='image')

    class Meta:
        model = Image
        fields = ['pk', 'image', 'created_at']
