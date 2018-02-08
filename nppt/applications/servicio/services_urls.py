from django.conf.urls import url, re_path

from . import viewsets



urlpatterns = [
        #url para servicios mas visitados
        re_path(r'^api/servicerecent/list/$',
            viewsets.ServiceRecentlyVisitViewset.as_view({'get': 'list'}),
            name='api_servicerecent-list'
        ),
        #url para servicios por destino
        re_path(r'^api/servicio/service/(?P<destino>[-\w]+)/$',
            viewsets.ServicebyDestinyViewset.as_view({'get': 'list'}),
            name='api_servicios-by-destiny'
        ),

]
