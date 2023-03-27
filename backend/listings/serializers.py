from rest_framework import serializers
from .models import Listings, PhotoListing


class PhotoListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhotoListing
        fields = ['photo']


class ListingsSerializer(serializers.ModelSerializer):
    photos_listing = serializers.SerializerMethodField(
        'get_listing_photo')

    class Meta:
        model = Listings
        fields = ['title', 'address', 'city', 'county', 'price', 'sale_type', 'property_type', 'bedrooms_number',
                  'floor_number', 'slug', 'photos_listing']

    def get_listing_photo(self, photo_listing):
        photo_listing_query = PhotoListing.objects.filter(listing_id=photo_listing.id)
        serializer = PhotoListingSerializer(photo_listing_query, many=True)

        return serializer.data


class ListingDetailSerializer(serializers.ModelSerializer):
    photos_listing = serializers.SerializerMethodField(
        'get_listing_photo')

    class Meta:
        model = Listings
        fields = '__all__'

    def get_listing_photo(self, photo_listing):
        photo_listing_query = PhotoListing.objects.filter(listing_id=photo_listing.id)
        serializer = PhotoListingSerializer(photo_listing_query, many=True)

        return serializer.data
