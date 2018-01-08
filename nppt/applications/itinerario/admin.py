from django.contrib import admin

# Register your models here.
from .models import Place, Itinerary


admin.site.register(Place)
admin.site.register(Itinerary)
