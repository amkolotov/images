from django.contrib import admin
from django.utils.html import format_html

from apps.main.models import Image


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'image_tag', 'image', 'created_at']
    ordering = ('-created_at', )
    readonly_fields = ('image_tag',)

    def image_tag(self, obj):
        return format_html(f'<img src="{obj.image.url}" />')
