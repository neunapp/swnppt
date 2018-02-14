from rest_framework import serializers

from .models import Service


class ServiceRecentlyVisitSerializer(serializers.ModelSerializer):
    """serializar para listar servicio recientemente utilizados """

    class Meta:

        model = Service
        fields =('__all__')
