
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

#model from other applications

from applications.servicio.models import Service



@python_2_unicode_compatible
class Place(TimeStampedModel):

    destiny =models.CharField('destino', max_length=100)
    name = models.CharField('nombre', max_length=100)
    title_seo = models.CharField('titulo seo', max_length=150)
    description = models.TextField('descripcion', blank=True)
    description_seo = models.CharField('descripcion seo', max_length=150)
    content = FroalaField()
    tags = models.CharField('Tags', max_length=100)
    visit = models.IntegerField('visitas')
    slug = models.SlugField(editable=False, max_length=200)

    class Meta:
        verbose_name = 'Lugar'
        verbose_name_plural = 'Lugares'
        ordering = ['-created']

    def __str__(self):
        return self.destiny

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
        super(Place, self).save(*args, **kwargs)


@python_2_unicode_compatible
class Itinerary(TimeStampedModel):

    denomination = models.CharField('denominacion', max_length=150)
    distance_foot = models.CharField('distancia pies', max_length=50)
    altitude_place = models.CharField('altitud del lugar', max_length=70)
    wheater = models.CharField('clima', max_length=70)
    description = models.TextField('descripcion', blank=True)
    place = models.ManyToManyField(Place)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Itinerario'
        verbose_name_plural = 'Itinerarios'
        ordering = ['-created']

    def __str__(self):
        return self.denomination
