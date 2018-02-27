
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

#model from other applications

from applications.servicio.models import Service, Destiny
from applications.blog.models import Tag



@python_2_unicode_compatible
class Place(TimeStampedModel):
    """ modelo para tabla lugar """

    destiny = models.ForeignKey(
        Destiny,
        on_delete=models.CASCADE,
        verbose_name='Destino',
    )
    image = models.ImageField(
        'Foto',
        upload_to="lugares",
        blank=True,
        null=True
    )
    name = models.CharField('nombre', max_length=100)
    title_seo = models.CharField('titulo seo', max_length=150)
    description = models.TextField('descripcion', blank=True)
    description_seo = models.CharField('descripcion seo', max_length=150)
    content = RichTextUploadingField('contenido')
    tags = models.ManyToManyField(Tag)
    visit = models.IntegerField('visitas', default=0)
    slug = models.SlugField(editable=False, max_length=200)

    class Meta:
        verbose_name = 'Lugar'
        verbose_name_plural = 'Lugares'
        ordering = ['-created']

    def __str__(self):
        return self.name

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
            slug_unique = '%s %s' % (self.name, str(seconds))
        else:
            seconds = self.slug.split('-')[-1]  # recuperamos los segundos
            slug_unique = '%s %s' % (self.name, str(seconds))

        self.slug = slugify(slug_unique)
        super(Place, self).save(*args, **kwargs)


@python_2_unicode_compatible
class Itinerary(TimeStampedModel):
    """ tabla para itinerario de un servicio """

    denomination = models.CharField(
        'denominacion', max_length=150
    )
    distance_foot = models.CharField(
        'distancia a pie',
        max_length=50,
        blank=True
    )
    altitude_place = models.CharField(
        'altitud del lugar',
        max_length=70,
        blank=True
    )
    wheater = models.CharField(
        'clima',
        max_length=70,
        blank=True
    )
    description = models.TextField('descripcion', blank=True)
    place = models.ManyToManyField(Place)
    service = models.ForeignKey(
        Service,
        verbose_name='Servicio',
        related_name='itinerarys',
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'Itinerario'
        verbose_name_plural = 'Itinerarios'
        ordering = ['-created']

    def __str__(self):
        return self.denomination
