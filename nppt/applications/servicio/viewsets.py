#libraries rest_framework
from rest_framework import viewsets
from rest_framework.response import Response

#models
from .models import Service

from .serializers import ServiceRecentlyVisitSerializer


class ServiceRecentlyVisitViewset(viewsets.ModelViewSet):
    """
        viewset que lista los 20 servicios mas recientes
    """
    serializer_class = ServiceRecentlyVisitSerializer

    def get_queryset(self):
        queryset = Service.objects.service_recent()
        return queryset



class ServicebyDestinyViewset(viewsets.ModelViewSet):
    """
        viewset que lista los 20 servicios mas recientes
    """
    serializer_class = ServiceRecentlyVisitSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        queryset = Service.objects.find_destiny_by_service(pk)
        return queryset