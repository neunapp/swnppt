from django.shortcuts import render
from django.views.generic import (
    ListView,
    TemplateView,
    DetailView,
    CreateView
)
from django.urls import reverse_lazy
# Create your views here.

#app blog
from applications.blog.models import Blog
#forms
from .forms import ContactUsForm

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


class ContactUsCreateView(CreateView):
    form_class = ContactUsForm
    success_url = '.'
    template_name = 'home/contacto.html'
