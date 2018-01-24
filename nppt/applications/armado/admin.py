from django.contrib import admin

# Register your models here.

from .models import Armed, ArmedDestiny, ItineraryDestiny

class ArmedAdmin(admin.ModelAdmin):
    """admin home model"""
    list_display = (
        'user',
        'date_start',
        'date_end',
        'arrival_time',
        'exit_time',
        'state',
    )
    #
    search_fields = ('user', 'state',)
    list_filter = ('user',)



class ArmedDestinyAdmin(admin.ModelAdmin):
    """admin home model"""
    list_display = (
        'armed',
        'destiny',
    )
    #
    search_fields = ('armed', 'destiny',)
    list_filter = ('armed',)



class ItineraryDestinyAdmin(admin.ModelAdmin):
    """admin home model"""
    list_display = (
        'armeddestiny',
        'date',
        'service',
    )
    #
    search_fields = ('armeddestiny',)
    list_filter = ('armeddestiny',)


admin.site.register(Armed, ArmedAdmin)
admin.site.register(ArmedDestiny, ArmedDestinyAdmin)
admin.site.register(ItineraryDestiny, ItineraryDestinyAdmin)

