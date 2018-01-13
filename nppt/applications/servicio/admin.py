from django.contrib import admin

# Register your models here.
from .models import Type_Service, Destiny, Service, Category_Service

admin.site.register(Type_Service)
admin.site.register(Destiny)
admin.site.register(Service)
admin.site.register(Category_Service)




