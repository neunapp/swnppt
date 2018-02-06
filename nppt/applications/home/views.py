from django.shortcuts import render

from django.views.generic import ListView, TemplateView, DetailView
# Create your views here.

#forms
from .forms import ContactUsForm

#models from other applicatoons
from applications.blog.models import Category, Blog

#forms from other applications
from applications.blog.forms import SearchForm

#
from .models import Home


class HomeView(TemplateView):
    """  vista que muestra la pagina principal """

    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        #contexto principal
        context['home'] = Home.objects.order_by('-created')[0]
        #proyectos sociales
        context['proyectos'] = Blog.objects.filter(
            category__model='3',
            published=True,
        ).order_by('-created')[:4]
        return context


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



class BLogListView(ListView):
    """
        vista que lista blog por categoria
    """
    context_object_name = 'blogs'
    template_name = 'home/list_blog.html'

    def get_context_data(self, **kwargs):
        context = super(BLogListView, self).get_context_data(**kwargs)
        context['form'] = SearchForm
        return context

    def get_queryset(self):
        # recuperamos el valor por GET
        blog = self.request.GET.get("kword", '')
        category = self.kwargs['category']
        queryset = Blog.objects.search_blog(blog, category)
        return queryset



class BLogDetailview(DetailView):
    """
    vista que muestra detalle blog
    """

    context_object_name = 'blogs'
    model = Blog
    template_name = 'home/detail_blog.html'


    def get_context_data(self, **kwargs):
        context = super(BLogDetailview, self).get_context_data(**kwargs)
        slug = self.kwargs['slug']
        context['blog'] = Blog.objects.search_blog_detail(slug)
        return context
