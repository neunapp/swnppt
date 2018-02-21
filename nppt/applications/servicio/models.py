
# standard library
from datetime import timedelta, datetime
# Create your models here.
#third party
from model_utils.models import TimeStampedModel
from ckeditor_uploader.fields import RichTextUploadingField

#django libraries

from django.db import models
from django.conf import settings
from django.utils.encoding import python_2_unicode_compatible
from django.template.defaultfilters import slugify

#import manager servicio
from .managers import ServiceManager


@python_2_unicode_compatible
class ExtraDetails(TimeStampedModel):

   name = models.CharField('nombre', max_length=150)
   order = models.PositiveIntegerField('orden', default=0)
   denomination = models.CharField('ID',blank=True, max_length=150)
   content = RichTextUploadingField('contenido', blank=True)

   class Meta:
       verbose_name = 'Detalles extra de un servicio'
       verbose_name_plural = 'Detalles extra de un servicio'
       ordering = ['-created']

   def __str__(self):
       return self.denomination+' ['+str(self.id)+']'


class Destiny(TimeStampedModel):

    city = models.CharField('ciudad', max_length=50)
    description = models.CharField('descripcion', max_length=200)
    hour_start = models.TimeField('hora comienzo')
    hour_end = models.TimeField('hora fin')

    class Meta:
        verbose_name = 'destino'
        verbose_name_plural = 'destinos'
        ordering = ['-created']

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.city = self.city.lower()
        return super(Destiny, self).save()

    def __str__(self):
        return self.city


class Service(TimeStampedModel):
    """ modelo para paquetes servicios """

    E = '4'
    D = '3'
    C = '2'
    B = '1'
    A = '0'
    TYPE_CHOICES = (
        (A, 'Tours Clasicos'),
        (B, 'Camino Inca'),
        (C, 'Caminatas Alternativas'),
        (D, 'Paqute Normal'),
        (E, 'Paqute simple'),
    )
    type_service = models.CharField(
        'tipo de servicio',
        max_length=2,
        blank=True,
        choices=TYPE_CHOICES
    )
    destiny = models.ForeignKey(
        Destiny,
        on_delete=models.CASCADE,
        verbose_name='Destino',
    )
    title = models.CharField('titulo', max_length=130)
    image = models.ImageField('imagen', upload_to="servicios")
    mapa = models.ImageField('mapa', upload_to="mapa", blank=True, null=True)
    days = models.IntegerField('dias', default=0)
    promo = models.BooleanField('Promocion', default=False)
    altitude_average = models.IntegerField('Altitud', default=0)
    description = models.TextField('descripcion', blank=True)
    include = RichTextUploadingField('incluye', blank=True)
    not_include = RichTextUploadingField('No incluye', blank=True)
    extra = models.ManyToManyField(ExtraDetails, verbose_name='detalles extra')
    tree = models.IntegerField('numero de arboles', default=0)
    private_price = models.DecimalField('Precio Privado', max_digits=7, decimal_places=2, default=0)
    shared_price = models.DecimalField('Precio Compartido', max_digits=7, decimal_places=2, default=0)
    difficulty = models.CharField('dificultad', max_length=50, blank=True)
    spa_trip = models.CharField('tipo excursion', max_length=150, blank=True)
    hour_start = models.TimeField('hora inicio', blank=True, null=True)
    hour_end = models.TimeField('hora Fin', blank=True, null=True)
    distance_total = models.CharField('distancia total', max_length=50, blank=True)
    recommended_for = models.CharField('recomendado para', max_length=200, blank=True)
    consideration = RichTextUploadingField('concideraciones', blank=True)
    state = models.BooleanField(default=False)
    visit = models.IntegerField(default=0, editable=False)
    slug = models.SlugField(editable=False, max_length=200)

    objects = ServiceManager()

    class Meta:
        verbose_name = 'servicio'
        verbose_name_plural = 'servicios'
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
        super(Service, self).save(*args, **kwargs)
