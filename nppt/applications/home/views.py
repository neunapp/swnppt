from django.shortcuts import render

from django.views.generic import ListView, TemplateView
# Create your views here.

#forms
from .forms import ContactUsForm

#models from other applicatoons
from applications.blog.models import Category

#forms from other applications
from applications.blog.forms import SearchForm

class CategoriaListView(ListView):
    """
    vista que lista caterias
    """

    context_object_name = 'categoryfind'
    template_name = 'home/list_category.html'

    def get_context_data(self, **kwargs):
        context = super(CategoriaListView, self).get_context_data(**kwargs)
        context['form'] = SearchForm
        context['category'] = Category.objects.list_category()
        context['formcontactus'] = ContactUsForm
        return context

    def get_queryset(self):
        # recuperamos el valor por GET
        category = self.request.GET.get("kword", '')
        queryset = Category.objects.search_category(category)
        return queryset
