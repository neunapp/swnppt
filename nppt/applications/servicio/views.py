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
#
from .models import Service


class ClasicToursView(ListView):
    """ vista que lista tours clasicos """

    context_object_name = 'servicios'
    template_name = 'servicios/tour_clasicos.html'

    def get_queryset(self):
        #recuperamos el valor por GET
        queryset = Service.objects.service_by_tipe('CT')
        return queryset


class AlternativeWalksView(ListView):
    """ vista que lista camintas alternativas """

    context_object_name = 'servicios'
    template_name = 'servicios/caminatas_alternativas.html'

    def get_queryset(self):
        #recuperamos el valor por GET
        queryset = Service.objects.service_by_tipe('AW')
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
