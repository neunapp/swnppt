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
        'days',
        'private_price',
        'shared_price',
        'spa_trip',
        'hour_start',
        'hour_end',
        'visit',
    )
    list_filter = ('type_service',)

admin.site.register(Type_Service)
admin.site.register(Destiny)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Category_Service, Category_ServiceAdmin)
