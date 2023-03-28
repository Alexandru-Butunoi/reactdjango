from django.db import models
from django.utils.timezone import now
from realtors.models import Realtor
from PIL import Image
# Create your models here.


class Listings(models.Model):
    class SaleType(models.TextChoices):
        SALE = 'For Sale'
        RENT = 'For Rent'

    class PropertyType(models.TextChoices):
        APARTMENT = 'Apartment'
        HOUSE = 'House'
        STUDIO_APARTMENT = 'Studio Apartment'
        COMMERCIAL_SPACE = 'Commercial Space'

    class Furnished(models.TextChoices):
        SEMI_FURNISHED ='Semi-furnished'
        FURNISHED_MODERN = 'Furnished with modern utilities'
        FURNISHED_CLASSIC = 'Furnished with classic utilities'
        LUX = 'Luxurious'

    class Parking(models.TextChoices):
        GARAGE = 'Garage'
        UNDERGROUND_GARAGE = 'Underground parking'
        EXTERIOR_PARKING = 'Exterior parking'
        SUBSCRIPTION_PARKING = 'Subscription parking'

    realtor = models.ForeignKey(Realtor, on_delete=models.CASCADE)
    title = models.CharField(max_length=155)
    slug = models.CharField(max_length=200, unique=True)
    address = models.CharField(max_length=150)
    city = models.CharField(max_length=100)
    county = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=15)
    description = models.TextField(blank=True)
    sale_type = models.CharField(max_length=50, choices=SaleType.choices, default=SaleType.SALE)
    property_type = models.CharField(max_length=100, choices=PropertyType.choices, default=PropertyType.APARTMENT)
    price = models.IntegerField()
    bedrooms_number = models.IntegerField(null=True, choices=((x, x) for x in range(1, 21)), blank=True,
                                          verbose_name='Bedrooms')
    bathrooms_number = models.IntegerField(null=True, choices=((x, x) for x in range(1, 11)), blank=True,
                                           verbose_name='Bathrooms')
    kitchens_number = models.IntegerField(null=True, choices=((x, x) for x in range(1, 6)), blank=True,
                                          verbose_name='Kitchens')
    balconies_number = models.IntegerField(null=True, choices=((x, x) for x in range(1, 11)), blank=True,
                                           verbose_name='Balconies')
    furnished = models.CharField(max_length=100, choices=Furnished.choices, default=Furnished.FURNISHED_MODERN,
                                 blank=True, verbose_name='Furnished')
    parking = models.CharField(max_length=100, choices=Parking.choices, default=Parking.GARAGE, blank=True,
                               verbose_name='Parking opportunity')
    construction_year = models.IntegerField(null=True, blank=True, verbose_name='Construction year')
    floor_number = models.IntegerField(null=True, choices=((x, x) for x in range(0, 21)), blank=True,
                                       verbose_name='Floor')
    sqm = models.IntegerField()
    is_published = models.BooleanField(default=True)
    listing_date = models.DateTimeField(default=now, blank=True)

    def __str__(self):
        return self.title


class PhotoListing(models.Model):
    listing = models.ForeignKey(Listings, on_delete=models.CASCADE, verbose_name='Photo')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d')

    def save(self, *args, **kwargs):
        super(PhotoListing, self).save(*args, **kwargs)
        img = Image.open(self.photo.path)
        if img.height > 1125 or img.width > 1125:
            img.thumbnail((1125, 1125))
        img.save(self.photo.path, quality=70, optimize=True)

    def __str__(self):
        return self.photo.path


