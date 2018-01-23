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

        return self.order_by('-type_name')


    def search_category(self, find):
        """ Procedimiento para buscar categoria"""

        # filtramos por nombre
        return self.filter(
            type_name__icontains=find,
        ).order_by('-type_name')[:20]


class BlogManager(models.Manager):
    """procedimiento para tabla blog"""

    def search_blog(self, name):
        """funcion que devuelve blogs mas visitados"""

        #filtramos por nombre
        return self.filter(
            title__icontains = name,
        ).order_by('-views')[:20]


    def search_blog_by_category(self, slug):
        #filtramos por nombre blog
        return self.filter(
            published=True,
            category__slug = slug,
        ).order_by('-views')[:20]





