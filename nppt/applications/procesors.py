from django.http import Http404

from applications.servicio.models import Service


# context procesor para devover servicios de tipo classic tour
def global_tour_clasicos(request):
    queryset = Service.objects.service_by_tipe('0','')[:10]
    return {'global_tc':queryset}


# context procesor para AlternativeWalksView
def global_camintas_alternativas(request):
    queryset = Service.objects.service_by_tipe('2','')[:10]
    return {'global_ca':queryset}


# context procesor para camino inca
def global_camino_inca(request):
    queryset = Service.objects.service_by_tipe('1','')[:10]
    return {'global_ci':queryset}

#context procesor para camino inca
def global_services(request):
    queryset = Service.objects.service_by_all_type('')[:10]
    return {'global_pt':queryset}
