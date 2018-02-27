from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include, re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    #url app home
    re_path(r'^', include('applications.home.urls')),
    #url app servicio
    re_path(r'^', include('applications.servicio.urls')),
    #url app itinerario
    re_path(r'^', include('applications.itinerario.urls')),
    #urls app blog
    re_path(r'^', include('applications.blog.urls')),
    # urls app user
    re_path(r'^', include('applications.users.urls')),

                  #url para editor de texto
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
