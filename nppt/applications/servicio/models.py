
# standard library
from datetime import timedelta, datetime
# Create your models here.
#third party
from model_utils.models import TimeStampedModel

#django libraries

from django.db import models
from django.conf import settings
from django.utils.encoding import python_2_unicode_compatible
from django.template.defaultfilters import slugify


@python_2_unicode_compatible
class Type_service(TimeStampedModel):

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
        verbose_name = 'descuento'
        verbose_name_plural = 'descuentos'
        ordering = ['-created']

    def __str__(self):
        return self.city


class Service(TimeStampedModel):

    type_service = models.ForeignKey(Type_service, on_delete=models.CASCADE)
    destiny = models.ForeignKey(Destiny, on_delete=models.CASCADE)
    title = models.CharField('titulo', max_length=100)
    image = models.URLField()
    days = models.IntegerField()
    altitude_average = models.IntegerField()
    description = models.CharField('descripcion', max_length=200)
    include = models.CharField('incluye', max_length=200)
    not_include = models.CharField('no incluye', max_length=200)
    private_price = models.CharField('precio privado', max_length=50)
    shared_price = models.CharField('precio compartido', max_length=50)
    difficulty = models.CharField('dificultad', max_length=50)
    spa_trip = models.CharField('spa excursion', max_length=150)
    hour_start = models.TimeField('hora inicio')
    hour_end = models.TimeField('hora inicio')
    distance_total = models.CharField('distancia total', max_length=50)
    recommended_for = models.CharField('recomendado para', max_length=200)
    consideration = models.CharField('consideraciones', max_length=200)
    state = models.BooleanField(default=True)
    visit = models.IntegerField()

    class Meta:
        verbose_name = 'servicio'
        verbose_name_plural = 'servicios'
        ordering = ['-created']

    def __str__(self):
        return self.title
