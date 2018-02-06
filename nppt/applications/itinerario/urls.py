from django.conf.urls import include, url, re_path
from . import views

app_name="itinerario_app"

urlpatterns = [
    # url para tours clasicos
    re_path(r'^los-mejores-atractivos-de-peru/(?P<slug>[-\w]+)$',
        views.PlaceDetailView.as_view(),
        name='place_detail'
    ),



    ####urls para servicos
    #re_path(r'^', include('applications.servicio.services_urls')),
]
