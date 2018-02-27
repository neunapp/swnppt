# standard library
from datetime import timedelta, datetime
# Create your models here.
#third party
from model_utils.models import TimeStampedModel
from ckeditor_uploader.fields import RichTextUploadingField

#django libraries
from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from django.conf import settings
from django.utils.encoding import python_2_unicode_compatible
from django.template.defaultfilters import slugify


#import manager
from .managers import SocialProjectManager, CategoryManager, BlogManager

@python_2_unicode_compatible
class Category(TimeStampedModel):

    A = '3'
    B = '2'
    C = '1'
    D = '0'
    E = '4'
    MODE_CHOICES = (
        (A, 'Proyectos Sociales'),
        (B, 'Preguntas Frecuentes'),
        (C, 'Empresa'),
        (D, 'Video'),
        (E, 'Otro'),
    )
    model = models.CharField(
        'modelo',
        max_length=2,
        blank=True,
        choices=MODE_CHOICES
    )
    type_name = models.CharField('tipo nombre', max_length=100)
    slug = models.SlugField(editable=False, max_length=200)
    objects =CategoryManager()

    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'
        ordering = ['-created']

    def __str__(self):
        return self.type_name

    def save(self, *args, **kwargs):
        if not self.id:
            # calculamos el total de segundos de la hora actual
            now = datetime.now()
            total_time = timedelta(
                hours=now.hour,
                minutes=now.minute,
                seconds=now.second
            )
            seconds = int(total_time.total_seconds())
            slug_unique = '%s %s' % (self.type_name, str(seconds))
        else:
            seconds = self.slug.split('-')[-1]  # recuperamos los segundos
            slug_unique = '%s %s' % (self.type_name, str(seconds))

        self.slug = slugify(slug_unique)
        super(Category, self).save(*args, **kwargs)



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
    """Modelo para Blog """

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title_seo = models.CharField('titulo seo', max_length=100)
    description_seo = models.CharField('descripcion seo', max_length=200)
    title = models.CharField('titulo', max_length=100)
    sub_title = models.CharField('subtitulo', max_length=200)
    description = models.TextField('Descripcion', blank=True)
    content = RichTextUploadingField('contenido')
    author = models.CharField('autor', max_length=200)
    image1 = models.ImageField('imagen uno', upload_to="blog")
    slug = models.SlugField(editable=False, max_length=200, null=True, blank=True)
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
    video = models.TextField(blank=True)
    tags = models.ManyToManyField(Tag)
    published = models.BooleanField(default=False)
    visits = models.IntegerField(default=0, editable=False)
    slug = models.SlugField(editable=False, max_length=200)
    objects = BlogManager()

    class Meta:
        verbose_name = 'blog'
        verbose_name_plural = 'blogs'
        ordering = ['-created']

    def __str__(self):
        return self.title


    def save(self, *args, **kwargs):
        if not self.id:
            # calculamos el total de segundos de la hora actual
            now = datetime.now()
            total_time = timedelta(
                hours=now.hour,
                minutes=now.minute,
                seconds=now.second
            )
            seconds = int(total_time.total_seconds())
            slug_unique = '%s %s' % (self.title, str(seconds))
        else:
            seconds = self.slug.split('-')[-1]  # recuperamos los segundos
            slug_unique = '%s %s' % (self.title, str(seconds))

        self.slug = slugify(slug_unique)
        super(Blog, self).save(*args, **kwargs)


@python_2_unicode_compatible
class Bloggeer(TimeStampedModel):
    """Modelo para Clientes Bloggeers """

    title = models.CharField('titulo', max_length=100)
    blog_link = models.URLField('Enlace a Blog', blank=True)
    image_link = models.URLField('Enlace de Imagen', blank=True)
    description = models.TextField('Descripcion', blank=True)
    tags = models.ManyToManyField(Tag)
    published = models.BooleanField(default=False)
    slug = models.SlugField(editable=False, max_length=200)

    class Meta:
        verbose_name = 'Bloggeers'
        verbose_name_plural = 'Bloggeers'
        ordering = ['-created']

    def __str__(self):
        return self.title


    def save(self, *args, **kwargs):
        if not self.id:
            # calculamos el total de segundos de la hora actual
            now = datetime.now()
            total_time = timedelta(
                hours=now.hour,
                minutes=now.minute,
                seconds=now.second
            )
            seconds = int(total_time.total_seconds())
            slug_unique = '%s %s' % (self.title, str(seconds))
        else:
            seconds = self.slug.split('-')[-1]  # recuperamos los segundos
            slug_unique = '%s %s' % (self.title, str(seconds))

        self.slug = slugify(slug_unique)
        super(Bloggeer, self).save(*args, **kwargs)


@python_2_unicode_compatible
class FrequentQestions(TimeStampedModel):
    """ Modelo para Registrar preguntas frecuentes """

    email = models.EmailField()
    question = models.TextField('Pregunta', blank=True)
    resuelt = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Preguntas'
        verbose_name_plural = 'Preguntas Frecuentes'
        ordering = ['-created']

    def __str__(self):
        return self.email
