from django.conf.urls import re_path

# local
from . import viewsets

app_name="users_services_url"

urlpatterns = [
    #api con registro de usuarios
    re_path(r'^api/users/registration/$',
            viewsets.UserAddViewset.as_view({'post': 'create'}),
            name='api_users-registration'
    ),

    #api que logea usuarios
    re_path(r'^api/users/login/$',
            viewsets.UserLoginViewset.as_view({'post': 'login'}),
            name='api_users-login'
    ),

    re_path(r'^api/users/email/$',
            viewsets.EmailVerificationViewset.as_view({'post': 'verification'}),
            name='api_users-email'
    ),
]