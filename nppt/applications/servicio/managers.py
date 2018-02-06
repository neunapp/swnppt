from django.db import models


class ServiceManager(models.Manager):
    """Procedimientos para tabla Service"""

    def service_by_tipe(self, tipo):
        # devolvemos los servicios dependiendo del tipo solicitado
        return self.filter(
            state=True,
            type_service__model=tipo,
        ).order_by('-visit')

    def service_visit(self):
        #"""Procedimiento para el tour con mas visitas"""
        visits = self.aggregate(models.Max('visit'))['visit__max']
        return self.filter(
            state=True,
            visit=visits)[:1]


    def service_recent(self):
        #"""procedimiento para adquirir los 20 servicios mas recientes"""
        return self.filter(
            state=True,
        ).order_by('-visit')[:20]


    def find_destiny_by_service(self, destiny):
        #procedimiento que busque servicio por destino
        return self.filter(
            destiny__city=destiny,
        ).order_by('-visit')[:20]
