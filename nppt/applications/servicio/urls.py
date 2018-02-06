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
    re_path(r'^alternative-walks-peru/$',
        views.AlternativeWalksView.as_view(),
        name='alternative_walks'
    ),
    #url para ver un servicio en detalle
    url(r'^viajes-peru/(?P<slug>[-\w]+)/$',
        views.ServiceDetailView.as_view(),
        name='service_detail'
    ),



    ####urls para servicos
    re_path(r'^', include('applications.servicio.services_urls')),
]
