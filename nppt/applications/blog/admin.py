from django.contrib import admin

from .models import Category, Tag, Blog
# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    list_display = (
     'category',
     'title_seo',
     'description_seo',
     'title',
     'sub_title',
     'description',
     'content',
     'author',
     'tags',
    )

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Blog)


