from django.contrib import admin

# Register your models here.
from .models import Destiny, Service, ExtraDetails

class ServiceAdmin(admin.ModelAdmin):
    list_display = (
        'type_service',
        'destiny',
        'title',
        'days',
        'private_price',
        'shared_price',
        'spa_trip',
        'hour_start',
        'hour_end',
        'visit',
    )
    list_filter = ('type_service',)
    filter_horizontal = ('extra',)

admin.site.register(Destiny)
admin.site.register(Service, ServiceAdmin)
admin.site.register(ExtraDetails)
