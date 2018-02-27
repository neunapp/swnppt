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



class UserLoginSerializer(serializers.ModelSerializer):
    """
        serializador para login user
    """
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = (
            'email',
            'password',
        )



class EmailVerificationSerializer(serializers.Serializer):
    """
        serializador para verificar si existe
    """

    email = serializers.EmailField()

