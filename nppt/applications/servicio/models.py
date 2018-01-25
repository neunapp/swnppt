
# standard library
from datetime import timedelta, datetime
# Create your models here.
#third party
from model_utils.models import TimeStampedModel
from froala_editor.fields import FroalaField

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
   slug = models.SlugField()

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

    def __str__(self):
        return self.city


class Service(TimeStampedModel):

    type_service = models.ForeignKey(Type_Service, on_delete=models.CASCADE)
    destiny = models.ForeignKey(Destiny, on_delete=models.CASCADE)
    title = models.CharField('titulo', max_length=100)
    image = models.ImageField('imagen', upload_to="destinos")
    days = models.IntegerField()
    promo = models.BooleanField('Promocion', default=False)
    altitude_average = models.IntegerField()
    description = models.TextField('descripcion', blank=True)
    include = FroalaField()
    not_include = FroalaField()
    tree = models.IntegerField('numero de arboles', default=0)
    private_price = models.CharField('precio privado', max_length=50)
    shared_price = models.CharField('precio compartido', max_length=50)
    difficulty = models.CharField('dificultad', max_length=50)
    spa_trip = models.CharField('spa excursion', max_length=150)
    hour_start = models.TimeField('hora inicio')
    hour_end = models.TimeField('hora inicio')
    distance_total = models.CharField('distancia total', max_length=50)
    recommended_for = models.CharField('recomendado para', max_length=200)
    consideration = FroalaField()
    service_categ11ory = models.ForeignKey(Category_Service, on_delete=models.CASCADE, null=True, blank=True)
    state = models.BooleanField(default=True)
    visit = models.IntegerField()

    objects = ServiceManager()

    class Meta:
        verbose_name = 'servicio'
        verbose_name_plural = 'servicios'
        ordering = ['-created']

    def __str__(self):
        return self.title
