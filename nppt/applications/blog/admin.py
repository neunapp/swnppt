from django.contrib import admin

from .models import Category, Tag, Blog, Social_Project
# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    list_display = (
     'category',
     'title_seo',
     'description_seo',
     'title',
     'sub_title',
     'description',
     'author',
    )
    list_filter = ('category',)
    # campos para agregar

    filter_horizontal = ('tags',)


class SocialProjectAdmin(admin.ModelAdmin):
    list_display = (
     'category',
     'title_seo',
     'description_seo',
     'title',
     'sub_title',
     'description',
     'author',
    )
    list_filter = ('category',)
    # campos para agregar

    filter_horizontal = ('tags',)


admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Social_Project, SocialProjectAdmin)


