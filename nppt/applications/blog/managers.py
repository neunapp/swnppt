from django.db import models

class SocialProjectManager(models.Manager):
    """
        procedimientos para tabla SOcial project
    """

    def search_Socical_project(self, num):
        """Consulta ah tabla social project"""

        return self.filter(
            importance = num
        )


class CategoryManager(models.Manager):
    """procedimientos para tabla category"""

    def list_category(self):
        """Consulta ah categorias de los blogs"""

        return self.order_by('-name_spa')


    def search_category(self, find):
        """ Procedimiento para buscar categoria"""

        # filtramos por nombre
        return self.filter(
            name_spa__icontains=find,
        ).order_by('-name_spa')[:20]

