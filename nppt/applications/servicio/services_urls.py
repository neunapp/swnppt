from django.conf.urls import url, re_path

from . import viewsets



urlpatterns = [
        #listar partidos
        re_path(r'^api/servicerecent/list/$',
            viewsets.ServiceRecentlyVisitViewset.as_view({'get': 'list'}),
            name='api_servicerecent-list'
        ),
        re_path(r'^api/servicio/service/(?P<pk>[-\w]+)/$',
            viewsets.ServicebyDestinyViewset.as_view({'get': 'list'}),
            name='api_servicios-by-destiny'
        ),

]

