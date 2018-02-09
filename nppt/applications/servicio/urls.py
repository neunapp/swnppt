from django.conf.urls import include, url, re_path
from . import views

app_name="servicio_app"

urlpatterns = [
    # url para tours clasicos
    re_path(r'^clasicc-tours-peru/$',
        views.ClasicToursView.as_view(),
        name='clasic_tours'
    ),
    #url para caminatas alternativas
    re_path(r'^camino-inca-y-otras-camintas-en-cusco/$',
        views.AlternativeWalksView.as_view(),
        name='alternative_walks'
    ),
    #url para servicios camino inca
    re_path(r'^camino-inca-cusco/$',
        views.CaminoIncaView.as_view(),
        name='camino_inca'
    ),
    #url para todo los servicios tipo paquete
    re_path(r'^paquetes-turisticos-economicos-en-peru/$',
        views.ServicesListView.as_view(),
        name='paquetes'
    ),
    #url para ver un servicio en detalle
    url(r'^viajes-peru/(?P<slug>[-\w]+)/$',
        views.ServiceDetailView.as_view(),
        name='service_detail'
    ),



    ####urls para servicos
    re_path(r'^', include('applications.servicio.services_urls')),
]
