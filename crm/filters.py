import django_filters
from .models import *


class CustomerFilter(django_filters.FilterSet):
    class Meta:
        model = Customer
        fields = ['name', 'status']

