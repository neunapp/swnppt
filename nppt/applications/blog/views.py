from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
# Create your views here.

# Create your views here.


#models from other applicatoons
from .models import Category, Blog

#forms from other applications
from .forms import SearchForm

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



class SearchGeneralBlogView(ListView):
    """
    vista que lista caterias
    """

    context_object_name = 'blogsgeneral'
    template_name = 'home/find_general_blog.html'

    def get_context_data(self, **kwargs):
        context = super(SearchGeneralBlogView, self).get_context_data(**kwargs)
        context['form'] = SearchForm
        context['blog'] = Blog.objects.all()
        return context

    def get_queryset(self):
        # recuperamos el valor por GET
        find = self.request.GET.get("kword", '')
        queryset = Blog.objects.search_general_blog(find)
        return queryset



