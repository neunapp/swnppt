from django.contrib import admin

# Register your models here.
from .models import Place, Itinerary

class PlaceAdmin(admin.ModelAdmin):
    """admin Place model"""
    list_display = (
        'destiny',
        'name',
        'title_seo',
        'description',
        'description_seo',
        'content',
        'visit',

    )
    #
    search_fields = ('destiny',)
    list_filter = ('destiny', 'name',)


class ItineraryAdmin(admin.ModelAdmin):
    """admin Itinerary model"""
    list_display = (
        'denomination',
        'distance_foot',
        'altitude_place',
        'description',
        'service',
    )
    #
    filter_horizontal = ('place',)
    search_fields = ('place',)

    list_filter = ('denomination',)


admin.site.register(Place, PlaceAdmin)
admin.site.register(Itinerary, ItineraryAdmin)
