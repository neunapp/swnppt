from django.contrib import admin

from .models import Values_enterprice, Home, Client_commentary
# Register your models here.


class Values_enterpriceAdmin(admin.ModelAdmin):
    """admin model values enterprice"""

    list_display = (
        'description_value',
    )

class HomeAdmin(admin.ModelAdmin):
    """admin home model"""
    list_display = (
        'title_seo',
        'description_seo',
        'phone1',
        'phone2',
        'phone3',
        'title_feature_enterprice',
        'sub_title',

    )
    #
    filter_horizontal = ('values_enterprice',)
    search_fields = ('title_seo',)
    list_filter = ('title_seo',)

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