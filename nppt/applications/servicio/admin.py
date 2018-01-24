from django.contrib import admin

# Register your models here.
from .models import Type_Service, Destiny, Service, Category_Service

class Category_ServiceAdmin(admin.ModelAdmin):

    """admin model cancha"""
    list_display = (
        'name',
    )

class ServiceAdmin(admin.ModelAdmin):
    list_display = (
        'type_service',
        'destiny',
        'title',
        'image',
        'days',
        'promo',
        'altitude_average',
        'description',
        'private_price',
        'shared_price',
        'spa_trip',
        'hour_start',
        'hour_end',
        'distance_total',
        'service_categ11ory',
        'visit',
    )
    list_filter = ('type_service',)
    # campos para agregar
    fields = (
        'type_service',
        'destiny',
        'title',
        'image',
        'days',
        'promo',
        'altitude_average',
        'description',
        'tree',
        'private_price',
        'shared_price',
        'difficulty',
        'spa_trip',
        'hour_start',
        'hour_end',
        'distance_total',
        'recommended_for',
        'consideration',
        'service_categ11ory',
        'visit',
    )



admin.site.register(Type_Service)
admin.site.register(Destiny)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Category_Service, Category_ServiceAdmin)




