from rest_framework.generics import ListAPIView
from ..models import Product
from .serializers import ProductSerializers
from django.db.models import Q
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class ModulPagination(PageNumberPagination):
    page_size = 5
    
    def get_paginated_response(self, data):
        return Response({
            'count': self.page.paginator.count,
            'total_pages': self.page.paginator.num_pages,
            'current_page': self.page.number,
            'results': data
        })

class ProductListApiView(ListAPIView):
    serializer_class = ProductSerializers
    pagination_class = ModulPagination

    def get_queryset(self):
        queryset = Product.objects.all()
        
        def apply_filter(param_name, field_name):
            param_value = self.request.query_params.get(param_name, None)
            if param_value:
                values = param_value.split(',')
                return Q(**{f"{field_name}__in": values})
            return None

        filters = [
            ('product_status', 'product_status'),
            ('product_property_type', 'product_property_type'),
            ('product_amenities', 'product_amenities'),
            ('product_price_range', 'product_price_range'),
            ('product_beth_patch', 'product_beth_patch')
        ]

        for param, field in filters:
            filter_query = apply_filter(param, field)
            if filter_query:
                queryset = queryset.filter(filter_query)
        queryset=queryset.order_by("-id")
        return queryset
