from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework import permissions
from .models import Listings
from .serializers import ListingDetailSerializer, ListingsSerializer
from django_filters import rest_framework as filters
from .filters import ListingsFilter
from datetime import datetime, timezone, timedelta


class ListingsView(ListAPIView):
    queryset = Listings.objects.order_by('-listing_date').filter(is_published=True)
    serializer_class = ListingsSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ListingsFilter
    permission_classes = (permissions.AllowAny, )


class ListingDetailView(RetrieveAPIView):
    queryset = Listings.objects.order_by('-listing_date').filter(is_published=True)
    serializer_class = ListingDetailSerializer


