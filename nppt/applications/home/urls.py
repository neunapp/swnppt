from django.conf.urls import include, re_path
from . import views

app_name = 'home_app'

urlpatterns = [
    #url para home
    re_path(r'^home/$',
        views.CategoriaListView.as_view(),
        name='category-list'
    ),
    re_path(r'^home/(?P<category>[-\w]+)/$',
        views.BLogListView.as_view(),
        name='blog-list'
    ),
    re_path(
        r'^blog/(?P<category>[-\w]+)/(?P<slug>[-\w]+)/$',
        views.BLogDetailview.as_view(),
        name='blog-detail'
    ),
]