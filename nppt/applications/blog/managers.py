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
        #"""Consulta ah categorias de los blogs"""

        return self.order_by('-type_name')


    def search_category(self, find):
        #""" Procedimiento para buscar categoria"""

        return self.filter(
            type_name__icontains=find,
        ).order_by('-type_name')[:20]


class BlogManager(models.Manager):
    """procedimiento para tabla blog"""

    def search_blog(self, blog, category):
        #"""funcion que devuelve blogs mas visitados"""
        return self.filter(
            title_seo__icontains=blog,
            category__slug=category
        ).order_by('-visit')[:20]


    def list_blog_by_category(self, slugcategory):
        #filtramos por nombre blog
        return self.filter(
            category__slug=slugcategory,
        ).order_by('-visit')[:20]


    def search_blog_detail(self, slug):
        # """funcion que devuelve detalle de blog"""
        return self.filter(
            slug=slug
        ).order_by('-visit')[:20]


    def search_general_blog(self, title_seo):
        #buscador de blog
        return self.filter(
            title_seo__icontains=title_seo,
        ).order_by('-visit')





