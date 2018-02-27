
#three party adds
from rest_framework import viewsets
from rest_framework.response import Response

#django libraries
from django.contrib.auth import authenticate, login

#model
from .models import User

#serializaor
from .serializers import UserAddSerializer, UserLoginSerializer, EmailVerificationSerializer



class UserAddViewset(viewsets.ViewSet):
    """
        Viewset para registrar usuario sin token
    """

    def create(self, request):

        serializado = UserAddSerializer(data=request.data)

        if serializado.is_valid():

            user = User(
                email=serializado.validated_data['email'],
                nacionality=serializado.validated_data['nacionality'],
                username=serializado.validated_data['email']
            )
            password = serializado.validated_data['password']
            if len(password) > 5:
                user.save()
                user.set_password(password)
                user.save()
                #creamos token de authentificacion
                respuesta = {'Usuario':'Agregado'}
            else:
                respuesta = {'contraseña':'contraseña mayor a 5 digitos'}
            respuesta = respuesta
        else:

            respuesta = serializado.errors

        return Response(respuesta)



class UserLoginViewset(viewsets.ViewSet):
    """
        viewset que logea usuario registrado sin token
    """

    def login(self, request):

        serializado = UserLoginSerializer(data=request.data)

        if serializado.is_valid():

            email = serializado.validated_data['email']
            password = serializado.validated_data['password']

            user = authenticate(email=email, password=password)

            if user is not None:
                json ={}
                if user.is_active:
                    login(self.request, user)
                    json['id'] = '1'

                response = json
            else:

                response = {'user':'usuario y/o contraseña no validos'}
        else:

                response = serializado.errors

        return Response(response)



class EmailVerificationViewset(viewsets.ViewSet):
    """
        verificar si usuario existe
    """

    def verification(self, request):

        serializado = EmailVerificationSerializer(data=request.data)

        if serializado.is_valid():

            email = serializado.validated_data['email']
            json = {}
            try:
                user = User.objects.get(email=email)
                json['id'] = '1'
            except User.DoesNotExist:
                json['id'] = '0'

            respuesta = json
        else:

            respuesta = serializado.errors

        return Response(respuesta)

