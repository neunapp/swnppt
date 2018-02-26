#libraries rest_framework
from rest_framework import viewsets
from rest_framework.response import Response

#models
from .models import Service, Destiny

from .serializers import (
    ServiceRecentlyVisitSerializer,
    DestinyListSerializer
)


class ServiceRecentlyVisitViewset(viewsets.ModelViewSet):
    """
        viewset que lista los 20 servicios mas recientes
    """
    serializer_class = ServiceRecentlyVisitSerializer

    def get_queryset(self):
        queryset = Service.objects.service_recent()[:3]
        return queryset


class DestinyListViewset(viewsets.ModelViewSet):
    """
        viewset que lista los destinos registrados
    """
    serializer_class = DestinyListSerializer

    def get_queryset(self):
        queryset = Destiny.objects.all()
        return queryset



class ServicebyDestinyViewset(viewsets.ModelViewSet):
    """
        viewset que lista los 20 servicios mas recientes
    """
    serializer_class = ServiceRecentlyVisitSerializer

    def get_queryset(self):
        destino = self.kwargs['destino']
        queryset = Service.objects.find_destiny_by_service(destino)
        return queryset
