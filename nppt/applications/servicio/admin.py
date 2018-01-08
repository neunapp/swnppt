from django.contrib import admin

# Register your models here.
from .models import Type_service, Destiny, Service

admin.site.register(Type_service)
admin.site.register(Destiny)
admin.site.register(Service)




