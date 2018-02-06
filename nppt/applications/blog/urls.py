from django.conf.urls import include, url, re_path
from . import views

app_name="blog_app"

urlpatterns = [
    # url para tours clasicos
    re_path(r'^recomendacion-para-viajar-a-peru/$',
        views.FrequentQestionsView.as_view(),
        name='frecuent_questions'
    ),
    #url para ver un blog en detalle
    re_path(r'^recomendacion-para-viajar-a-cusco-peru/(?P<slug>[-\w]+)/$',
        views.PFDetailView.as_view(),
        name='pf_detail'
    ),
    #url para listar proyectos sociales
    re_path(r'^proyectos-sociales-en-comunidades-de-cusco/$',
        views.PSListView.as_view(),
        name='ps_list'
    ),
    #url para ver un servicio en detalle
    re_path(r'^proyectos-sociales-cusco/(?P<slug>[-\w]+)/$',
        views.PSDetailView.as_view(),
        name='ps_detail'
    ),
    #url para listar bloggers
    re_path(r'^sobre-los-tours-en-peru/$',
        views.BlogListView.as_view(),
        name='blog_list'
    ),
    #url para ver un blog en detalle
    re_path(r'^conoce-mas-de-peru/(?P<slug>[-\w]+)/$',
        views.BlogDetailView.as_view(),
        name='blog_detail'
    ),


    ####urls para servicos
    re_path(r'^', include('applications.servicio.services_urls')),
]
