from rest_framework import serializers

from .models import Service


class ServiceRecentlyVisitSerializer(serializers.ModelSerializer):
    """serializar para listar servicio recientemente utilizados """

    class Meta:

        model = Service
        fields =(
            'type_service',
            'destiny',
            'title',
            'image',
            'days',
            'promo',
            'altitude_average',
            'description',
            'include',
            'not_include',
            'tree',
            'private_price',
            'shared_price',
            'difficulty',
            'spa_trip',
            'hour_start',
            'hour_end',
            'distance_total',
            'recommended_for',
            'consideration',
            'service_categ11ory',
            'state',
            'visit',
        )

