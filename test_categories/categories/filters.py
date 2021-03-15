import django_filters
from .models import Product
from django.db.models import Q 


class ProductFilter(django_filters.FilterSet):
    class Meta:
        model = Product
        fields = {
                'a': ['exact',],
                'b': ['icontains',],
                'c': ['lt', 'gt']
                }


