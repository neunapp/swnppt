from rest_framework import serializers

from .models import Service, Destiny


class ServiceRecentlyVisitSerializer(serializers.ModelSerializer):
    """serializar para listar servicio recientemente utilizados """

    class Meta:

        model = Service
        fields =('__all__')


class DestinyListSerializer(serializers.ModelSerializer):
    """serializar para listar destinos registrados"""

    class Meta:

        model = Destiny
        fields =('__all__')
