
# standard library
from datetime import timedelta, datetime
# Create your models here.
#third party
from model_utils.models import TimeStampedModel
from froala_editor.fields import FroalaField

#django libraries
from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from django.conf import settings
from django.utils.encoding import python_2_unicode_compatible
from django.template.defaultfilters import slugify


@python_2_unicode_compatible
class Category(TimeStampedModel):

    model = models.CharField('modelos', max_length=200)
    name_spa = models.CharField('nombre spa', max_length=100)

    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'
        ordering = ['-created']

    def __str__(self):
        return self.model


@python_2_unicode_compatible
class Tag(TimeStampedModel):
    name = models.CharField('nombre', max_length=150)

    class Meta:
        verbose_name = 'tag'
        verbose_name_plural = 'tags'
        ordering = ['-created']

    def __str__(self):
        return self.name

@python_2_unicode_compatible
class Blog(TimeStampedModel):

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title_seo = models.CharField('titulo seo', max_length=100)
    description_seo = models.CharField('descripcion seo', max_length=200)
    title = models.CharField('titulo', max_length=100)
    sub_title = models.CharField('subtitulo', max_length=200)
    description = models.CharField('descripcion', max_length=200)
    content = FroalaField()
    author = models.CharField('autor', max_length=200)
    image1 = models.ImageField('imagen uno', upload_to="blog")
    image2 = models.ImageField(
        'imagen dos',
        upload_to="blog",
        blank=True,
        null=True
    )
    image3 = models.ImageField(
        'imagen tres',
        upload_to="blog",
        blank=True,
        null=True
    )
    tags = models.ManyToManyField(Tag)

    class Meta:
        verbose_name = 'blog'
        verbose_name_plural = 'blogs'
        ordering = ['-created']

    def __str__(self):
        return self.title_seo

@python_2_unicode_compatible
class Social_Project(TimeStampedModel):
   MUY_ALTO= '3'
   ALTO = '2'
   MEDIO = '1'
   BAJO= '0'
   MODE_CHOICES = (
       (MUY_ALTO, 'Muy alto'),
       (ALTO, 'Alto'),
       (MEDIO, 'Medio'),
       (BAJO, 'Bajo'),
   )
   # se cambia por choises
   importance = models.CharField(
        'importancia',
        max_length=2,
        blank=True,
        choices=MODE_CHOICES
   )
   video = models.URLField('movie')
   category = models.ForeignKey(Category, on_delete=models.CASCADE)
   title_seo = models.CharField('titulo seo', max_length=100)
   description_seo = models.CharField('descripcion seo', max_length=200)
   title = models.CharField('titulo', max_length=100)
   sub_title = models.CharField('subtitulo', max_length=200)
   description = models.CharField('descripcion', max_length=200)
   content = FroalaField()
   author = models.CharField('autor', max_length=200)
   image1 = models.ImageField('imagen uno', upload_to="blog")
   image2 = models.ImageField(
       'imagen dos',
       upload_to="blog",
       blank=True,
       null=True
   )

   image3 = models.ImageField(
       'imagen tres',
       upload_to="blog",
       blank=True,
       null=True
   )
   tags = models.ManyToManyField(Tag)

   class Meta:
       verbose_name = 'Proyeccion social'
       verbose_name_plural = 'Proyecciones sociales'
       ordering = ['-created']

   def __str__(self):
       return self.title_seo

