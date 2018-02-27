
#three party adds
from rest_framework import viewsets
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

#model
from .models import User

#serializaor
from .serializers import UserAddSerializer



class UserAddViewset(viewsets.ViewSet):
    """
        Viewset para registrar usuario
    """

    def create(self, request):

        serializado = UserAddSerializer(data=request.data)

        if serializado.is_valid():
            user = User(
                email=serializado.validated_data['email'],
                nacionality=serializado.validated_data['nacionality'],
            )
            user.save()
            #actualizamos el password
            password = serializado.validated_data('password')
            user.set_password(password)
            user.save()
            #creamos token de authentificacion
            token = Token.objects.create(user=user)
        else:
            print('Error')
            token = 'Error'

        return Response(token)