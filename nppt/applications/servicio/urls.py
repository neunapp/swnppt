from django.conf.urls import include, url, re_path
from . import views

app_name="servicio_app"

urlpatterns = [
    #urls para vistas
    ####urls para servicos
    re_path(r'^', include('applications.servicio.services_urls')),
]
