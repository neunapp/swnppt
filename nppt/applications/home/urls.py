# -*- coding: utf-8 -*-
from django.conf.urls import include, url, re_path
from . import views

app_name="home_app"

urlpatterns = [
    #url para formulario de contacto
    re_path(r'^$',
        views.HomeView.as_view(),
        name='index'
    ),
    # url para tours clasicos
    re_path(r'^peru-private-tours-contacto/$',
        views.ContactUsCreateView.as_view(),
        name='home_contact'
    ),
]
