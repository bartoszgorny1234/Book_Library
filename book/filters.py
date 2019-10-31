import django_filters
from django.db import models
from .models import Book, Author
from partial_date import PartialDate
import datetime


class BookFilter(django_filters.FilterSet):
    published_date = django_filters.DateFromToRangeFilter(field_name='published_date')
    class Meta:
        model = Book
        fields = {
            'title': ['icontains'],
            'language': ['exact'],
            'authors__name': ['icontains'],
        }
