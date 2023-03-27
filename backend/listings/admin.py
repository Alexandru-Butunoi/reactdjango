from django.contrib import admin
from .models import PhotoListing, Listings


class PhotoAdmin(admin.StackedInline):
    model = PhotoListing


class ListingsAdmin(admin.ModelAdmin):
    inlines = [PhotoAdmin]

    class Meta:
        model = Listings


admin.site.register(PhotoListing)
admin.site.register(Listings, ListingsAdmin)
