from django.contrib import admin
from .models import PhotoListing, Listings


class PhotoAdmin(admin.StackedInline):
    model = PhotoListing


class ListingsAdmin(admin.ModelAdmin):
    inlines = [PhotoAdmin]
    list_filter = ('realtor', )
    list_editable = ('is_published', )
    list_display = ('id', 'title', 'price', 'realtor', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('realtor', )

    class Meta:
        model = Listings


admin.site.register(PhotoListing)
admin.site.register(Listings, ListingsAdmin)
