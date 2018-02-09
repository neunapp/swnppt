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

#from app itinerario
from applications.itinerario.models import Itinerary
from applications.blog.models import Blog
from applications.home.models import Home
#
from .models import Service
from .forms import SearchServiceForm


class ClasicToursView(ListView):
    """ vista que lista tours clasicos """

    context_object_name = 'servicios'
    template_name = 'servicios/tour_clasicos.html'

    def get_queryset(self):
        #recuperamos el valor por GET
        queryset = Service.objects.service_by_tipe('0','')
        return queryset


class AlternativeWalksView(ListView):
    """ vista que lista camintas alternativas """

    context_object_name = 'servicios'
    template_name = 'servicios/caminatas_alternativas.html'

    def get_context_data(self, **kwargs):
        context = super(AlternativeWalksView, self).get_context_data(**kwargs)
        #contexto principal
        context['form'] = SearchServiceForm
        return context

    def get_queryset(self):
        #recuperamos el valor por GET
        q = self.request.GET.get("kword", '')
        #consultas
        queryset = Service.objects.service_by_tipe('2','')
        proyectos = Blog.objects.list_by_category('','3').order_by('-created')[:4]
        return {'queryset':queryset, 'proyectos':proyectos}


class CaminoIncaView(ListView):
    """ vista que lista servicios camino inca"""

    context_object_name = 'servicios'
    template_name = 'servicios/camino_inka.html'

    def get_context_data(self, **kwargs):
        context = super(CaminoIncaView, self).get_context_data(**kwargs)
        #contexto principal
        context['form'] = SearchServiceForm
        return context

    def get_queryset(self):
        #recuperamos el valor por GET
        q = self.request.GET.get("kword", '')
        #consultas
        queryset = Service.objects.service_by_tipe('1',q)
        proyectos = Blog.objects.list_by_category('','3').order_by('-created')[:4]
        return {'queryset':queryset, 'proyectos':proyectos}


class ServicesListView(ListView):
    """ vista que lista todos los servicios"""

    context_object_name = 'servicios'
    template_name = 'servicios/list.html'

    def get_context_data(self, **kwargs):
        context = super(ServicesListView, self).get_context_data(**kwargs)
        #contexto principal
        context['form'] = SearchServiceForm
        context['home'] = Home.objects.order_by('-created')[0]
        return context

    def get_queryset(self):
        #recuperamos el valor por GET
        q = self.request.GET.get("kword", '')
        #consultas
        queryset = Service.objects.service_by_all_type(q)
        return queryset


class ServiceDetailView(DetailView):
    model = Service
    template_name = 'servicios/detail.html'

    def get_context_data(self, **kwargs):
        context = super(ServiceDetailView, self).get_context_data(**kwargs)
        #contexto principal
        itinerarios = Itinerary.objects.filter(
            service=self.get_object(),
        ).order_by('denomination')
        #
        context['itinerario'] = itinerarios
        context['proyectos'] = Blog.objects.filter(
            category__model='3',
            published=True,
        ).order_by('-created')[:4]
        return context
