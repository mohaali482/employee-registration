from rest_framework import pagination
from rest_framework.response import Response


class PagePagination(pagination.PageNumberPagination):

    def get_paginated_response(self, data):
        return Response({
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'current': self.page.number,
            'count': self.page.paginator.count,
            'start_index': self.page.start_index(),
            'total_pages': self.page.paginator.num_pages,
            'results': data
        })
