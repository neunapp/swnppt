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

#from models the other applications

from applications.users.models import User
from applications.servicio.models import Destiny, Service



@python_2_unicode_compatible
class Armed(TimeStampedModel):

    STARTED = '0'
    EDITION = '1'
    FINISHED = '2'

    MODE_CHOICES = (
        (STARTED, 'comienzo'),
        (EDITION, 'edicion'),
        (FINISHED, 'terminado'),

    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_start = models.DateField('hora inicio')
    date_end = models.DateField('hora fin')
    arrival_time = models.TimeField('tiempo de arribo')
    exit_time = models.TimeField('tiempo de salida')
    state = models.CharField(
        'estado',
        max_length=2,
        blank=True,
        choices=MODE_CHOICES
    )

    class Meta:
        verbose_name = 'Armado'
        verbose_name_plural = 'Armados'
        ordering = ['-created']

    def __str__(self):
        return self.user



@python_2_unicode_compatible
class ArmedDestiny(TimeStampedModel):

    armed = models.ForeignKey(Armed, on_delete=models.CASCADE)
    destiny = models.ForeignKey(Destiny, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'destino armado'
        verbose_name_plural = 'destinos armados'
        ordering = ['-created']

    def __str__(self):
        return self.armed



@python_2_unicode_compatible
class ItineraryDestiny(TimeStampedModel):

    armeddestiny = models.ForeignKey(ArmedDestiny, on_delete=models.CASCADE)
    date = models.DateField('Fecha')
    service = models.ForeignKey(Service, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'itinerario destino'
        verbose_name_plural = 'itinerarios destino'
        ordering = ['-created']

    def __str__(self):
        return self.armeddestiny

