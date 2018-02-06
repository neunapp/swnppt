# -*- coding: utf-8 -*-
from __future__ import unicode_literals
#django library
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.views.generic import (
    CreateView,
    UpdateView,
    DetailView,
    DeleteView,
    ListView,
    TemplateView,
    View,
)
from django.views.generic.edit import FormView

#
from .models import Blog, Bloggeer
from .forms import SearchForm, FrequentQestionsForm


class BlogListView(ListView):
    """ vista que lista los articulos de la empresa """

    context_object_name = 'blogs'
    template_name = 'blog/blog_list.html'

    def get_context_data(self, **kwargs):
        context = super(BlogListView, self).get_context_data(**kwargs)
        #proyectos sociales
        context['bloggers'] = Bloggeer.objects.all().order_by('-created')[:8]
        #enviamos formulario
        context['form'] = SearchForm
        return context

    def get_queryset(self):
        #recuperamos el valor por GET
        q = self.request.GET.get("kword", '')
        #
        queryset = Blog.objects.list_by_category(q, '1')[:12]
        return queryset


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog/blog_detail.html'

    def get_context_data(self, **kwargs):
        context = super(BlogDetailView, self).get_context_data(**kwargs)
        #proyectos sociales
        context['proyectos_sociales'] = Blog.objects.list_by_category('', '1')[:4]
        return context


class FrequentQestionsView(CreateView):
    """ vista que lista peguntas frecuentes """

    form_class = FrequentQestionsForm
    success_url = '.'
    template_name = 'blog/preguntas_frecuentes.html'

    def get_context_data(self, **kwargs):
        context = super(FrequentQestionsView, self).get_context_data(**kwargs)
        #enviamos formulario
        context['form2'] = SearchForm
        q = self.request.GET.get("kword", '')
        context['preguntas_frecuentes'] = Blog.objects.list_by_category(q, '2')[:12]
        return context


class PFDetailView(DetailView):
    model = Blog
    template_name = 'blog/pf_detail.html'

    def get_context_data(self, **kwargs):
        context = super(PFDetailView, self).get_context_data(**kwargs)
        #proyectos sociales
        context['proyectos_sociales'] = Blog.objects.list_by_category('', '1')[:4]
        return context


class PSListView(ListView):
    """ vista que lista blog de tipo proyecto social """

    context_object_name = 'proyectos_sociales'
    template_name = 'blog/ps_list.html'

    def get_context_data(self, **kwargs):
        context = super(PSListView, self).get_context_data(**kwargs)
        #enviamos formulario
        context['form'] = SearchForm
        return context

    def get_queryset(self):
        #recuperamos el valor por GET
        q = self.request.GET.get("kword", '')
        #
        queryset = Blog.objects.list_by_category(q, '3')[:9]
        return queryset


class PSDetailView(DetailView):
    model = Blog
    template_name = 'blog/ps_detail.html'

    def get_context_data(self, **kwargs):
        context = super(PSDetailView, self).get_context_data(**kwargs)
        #proyectos sociales
        context['proyectos_sociales'] = Blog.objects.filter(
            category__model='3',
            published=True,
        ).order_by('-created')[:4]
        return context
