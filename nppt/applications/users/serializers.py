from rest_framework import serializers

from .models import User



class UserAddSerializer(serializers.ModelSerializer):
    """
        serializador para model User
    """

    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = (
            'email',
            'nacionality',
            'password',
        )
