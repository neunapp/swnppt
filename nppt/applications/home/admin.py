from django.contrib import admin

from .models import Values_enterprice, Home, Client_commentary, ContactUs
# Register your models here.


class Values_enterpriceAdmin(admin.ModelAdmin):
    """admin model values enterprice"""

    list_display = (
        'description_value',
    )


class HomeAdmin(admin.ModelAdmin):
    """admin home model"""
    list_display = (
        'title',
        'description_seo',
    )
    #
    filter_horizontal = ('values_enterprice',)
    search_fields = ('title',)


class Client_commentaryAdmin(admin.ModelAdmin):
    """admin home model"""
    list_display = (
        'client_name',
        'commentary',
    )
    #
    search_fields = ('client_name',)
    list_filter = ('client_name',)


admin.site.register(Values_enterprice, Values_enterpriceAdmin)
admin.site.register(Home, HomeAdmin)
admin.site.register(Client_commentary, Client_commentaryAdmin)
admin.site.register(ContactUs)
