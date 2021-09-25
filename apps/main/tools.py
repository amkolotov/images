from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from config import settings


class ImagePageNumberPagination(PageNumberPagination):
    page_size = settings.PAGE_SIZE
    max_page_size = settings.MAX_PAGE_SIZE

    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'count_pages': self.page.paginator.num_pages,
            'results': data
        })
