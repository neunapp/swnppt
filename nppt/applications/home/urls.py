from django.conf.urls import include, re_path
from . import views

app_name = 'home_app'

urlpatterns = [
    #url para home
    re_path(r'^home/$',
        views.CategoriaListView.as_view(),
        name='blog-list'
    ),
]