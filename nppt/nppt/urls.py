#
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include, re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^', include('applications.home.urls')),
    re_path(r'^', include('applications.servicio.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
