from django.contrib import admin

from .models import Category, Tag, Blog, Bloggeer, FrequentQestions
# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    list_display = (
        'title_seo',
        'category',
        'title',
        'author',
    )
    list_filter = ('category',)
    # campos para agregar

    filter_horizontal = ('tags',)


class BloggeerAdmin(admin.ModelAdmin):
    list_display = (
     'title',
     'published',
    )
    # campos para agregar
    filter_horizontal = ('tags',)


class FrequentQestionsAdmin(admin.ModelAdmin):
    list_display = (
     'email',
     'question',
     'resuelt',
    )


admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Bloggeer, BloggeerAdmin)
admin.site.register(FrequentQestions, FrequentQestionsAdmin)
