from django.contrib import admin

# Register your models here
from .models import Discount_offert, Client, Sale, Detail_sale


class Discount_offertAdmin(admin.ModelAdmin):
     """admin Itinerary model"""
     list_display = (
         'name',
         'offert_code',
         'description',
         'date_limit',
         'use_number',
     )
     #
     search_fields = (
         'name',
         'offert_code',
         'use_number',
     )
     list_filter = ('name', 'offert_code', 'date_limit','use_number')



class ClientAdmin(admin.ModelAdmin):
     """admin Itinerary model"""
     list_display = (
         'user',
         'skype',
         'country',
         'city',
     )
     #
     search_fields = (
         'user',
         'country',
         'city',
     )
     list_filter = ('user', 'country', 'city',)




admin.site.register(Discount_offert, Discount_offertAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Sale)
admin.site.register(Detail_sale)
