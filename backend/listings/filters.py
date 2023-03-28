from rest_framework import generics
from django_filters import rest_framework as filters

from .models import Listings


class ListingsFilter(filters.FilterSet):

    sale_type = filters.MultipleChoiceFilter(choices=Listings.SaleType.choices, null_label='Any', null_value='')
    property_type = filters.MultipleChoiceFilter(choices=Listings.PropertyType.choices, null_label='Any', null_value='')
    furnished = filters.MultipleChoiceFilter(choices=Listings.Furnished.choices, null_value='')
    parking = filters.MultipleChoiceFilter(choices=Listings.Parking.choices, null_value='')
    min_price = filters.NumberFilter(field_name='price', lookup_expr='gte')
    max_price = filters.NumberFilter(field_name='price', lookup_expr='lte')
    min_bedrooms = filters.NumberFilter(field_name='bedrooms_number', lookup_expr='gte')
    max_bedrooms = filters.NumberFilter(field_name='bedrooms_number', lookup_expr='lte')
    min_bathrooms = filters.NumberFilter(field_name='bathrooms_number', lookup_expr='gte')
    max_bathrooms = filters.NumberFilter(field_name='bathrooms_number', lookup_expr='lte')
    min_kitchens = filters.NumberFilter(field_name='kitchens_number', lookup_expr='gte')
    max_kitchens = filters.NumberFilter(field_name='kitchens_number', lookup_expr='lte')
    min_balconies = filters.NumberFilter(field_name='balconies_number', lookup_expr='gte')
    max_balconies = filters.NumberFilter(field_name='balconies_number', lookup_expr='lte')
    min_sqm = filters.NumberFilter(field_name='sqm', lookup_expr='gte')
    max_sqm = filters.NumberFilter(field_name='sqm', lookup_expr='lte')

    class Meta:
        model = Listings
        fields = ['title', 'address', 'city', 'county', 'price', 'sale_type', 'property_type', 'bedrooms_number',
                  'floor_number', 'slug']
