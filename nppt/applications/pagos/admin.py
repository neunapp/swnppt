from django.contrib import admin

# Register your models here.

from .models import Discount_offert, Client, Sale, Detail_sale

admin.site.register(Discount_offert)
admin.site.register(Client)
admin.site.register(Sale)
admin.site.register(Detail_sale)
