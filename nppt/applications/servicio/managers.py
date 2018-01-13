from django.db import models


class ServiceManager(models.Manager):
    """Procedimientos para tabla Service"""

    def service_visit(self):
        """Procedimiento para el tour con mas visitas"""
        visits = self.aggregate(models.Max('visit'))['visit__max']
        return self.filter(
            state = True,
            visit = visits)[:1]


    def service_recent(self):
        """procedimiento para adquirir los 20 servicios mas recientes"""
        return self.filter(
            state = True
        ).order_by('-created')[:20]








        



