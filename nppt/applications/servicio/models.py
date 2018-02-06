
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
class Category_Service(TimeStampedModel):

   name = models.CharField('nombre', max_length=150)
   slug = models.SlugField(editable=False, max_length=200)

   class Meta:
       verbose_name = 'Categoria servicio'
       verbose_name_plural = 'Categorias servicio'
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
       super(Category_Service, self).save(*args, **kwargs)




@python_2_unicode_compatible
class Type_Service(TimeStampedModel):

    model = models.CharField('modelo', max_length=200)
    name = models.CharField('nombre', max_length=200)

    class Meta:
        verbose_name = 'tipo de servicio'
        verbose_name_plural = 'tipos de servicio'
        ordering = ['-created']

    def __str__(self):
        return self.model



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

    type_service = models.ForeignKey(
        Type_Service,
        on_delete=models.CASCADE,
        verbose_name='Tipo de Servicio',
    )
    destiny = models.ForeignKey(
        Destiny,
        on_delete=models.CASCADE,
        verbose_name='Destino',
    )
    title = models.CharField('titulo', max_length=130)
    image = models.ImageField('imagen', upload_to="destinos")
    days = models.IntegerField('dias', default=0)
    promo = models.BooleanField('Promocion', default=False)
    altitude_average = models.IntegerField('Altitud', default=0)
    description = models.TextField('descripcion', blank=True)
    include = RichTextUploadingField('incluye', blank=True)
    not_include = RichTextUploadingField('No incluye', blank=True)
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
    service_categ11ory = models.ForeignKey(
        Category_Service,
        verbose_name='Cetgoria de servicio',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
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
