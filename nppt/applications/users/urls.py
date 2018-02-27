# django
from django.conf.urls import include, re_path

from .views import UserAddView, LogoutView, UserLoginView


# local
app_name="users_app"

urlpatterns = [
    #urls para vistas
    ####urls para servicos
    re_path(
        r'^registro/$',
        UserAddView.as_view(),
        name='user-add'
    ),
    #url para login de usuarios
    re_path(
        r'^login/$',
        UserLoginView.as_view(),
        name='user-login'
    ),
    #url para cerrar sesion
    re_path(
        r'^salir/$',
        LogoutView.as_view(),
        name='logout'
    ),

    re_path(r'^', include('applications.users.services_urls')),
]