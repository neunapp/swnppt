# -*- coding: utf-8 -*-
from __future__ import unicode_literals
#django library
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.views.generic import (
    DetailView,
    ListView,
    TemplateView,
    View,
)

#from app itinerario
from applications.blog.models import Blog
#
from .models import Place


class PlaceDetailView(DetailView):
    model = Place
    template_name = 'itinerario/lugar/detail.html'

    def get_context_data(self, **kwargs):
        context = super(PlaceDetailView, self).get_context_data(**kwargs)
        place = self.get_object()
        #incrementamos la visita
        place.visit = place.visit + 1
        place.save()
        #
        context['lugares'] = Place.objects.all().order_by('-visit')[:4]
        return context
