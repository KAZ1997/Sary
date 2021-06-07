import django_filters
from django_filters import DateFilter, ChoiceFilter, ModelChoiceFilter
from django import forms
from .models import *


class TableFilter(django_filters.FilterSet):
    class Meta:
        model: Table
        fields = ['table_number', 'number_of_seats']
