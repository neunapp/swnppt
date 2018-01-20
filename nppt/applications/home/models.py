
# standard library
from datetime import timedelta, datetime
# Create your models here.
#third party
from model_utils.models import TimeStampedModel

#django libraries
from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from django.conf import settings
from django.utils.encoding import python_2_unicode_compatible
from django.template.defaultfilters import slugify

#model from other applications

from applications.servicio.models import Destiny


@python_2_unicode_compatible
class Values_enterprice(TimeStampedModel):

    description_value = models.CharField('valor de la empresa', max_length=200)

    class Meta:
        verbose_name = 'valor'
        verbose_name_plural = 'valores'
        ordering = ['-created']

    def __str__(self):
        return self.description_value



@python_2_unicode_compatible
class Home(TimeStampedModel):

   title_seo = models.CharField('titulo seo', max_length=200)
   description_seo = models.CharField('descripcion seo', max_length=10)
   banner_img = models.URLField('Imagen banner', blank=True, null=True)
   logo_img = models.URLField('Imagen logo', blank=True, null=True)
   phone1 = models.CharField('Celular 1', max_length=15)
   phone2 = models.CharField('Celular 2', max_length=15)
   phone3 = models.CharField('Celular 3', max_length=15)
   link_face = models.URLField('Facebook', blank=True, null=True)
   link_instagram = models.URLField('instragram', blank=True, null=True)
   link_youtube = models.URLField('youtube', blank=True, null=True)
   link_tripadvisor = models.URLField('tripadvisor', blank=True, null=True)
   title_feature_enterprice = models.CharField('titulo caracteristica empresa', max_length=200)
   values_enterprice = models.ManyToManyField(Values_enterprice)
   sub_title = models.CharField('subtitulo', max_length=100)
   description = models.CharField('descripcion', max_length=200)

   class Meta:
       verbose_name = 'titulo seo'
       verbose_name_plural = 'titulos seo'
       ordering = ['-created']

   def __str__(self):
       return self.title_seo



@python_2_unicode_compatible
class Client_commentary(TimeStampedModel):

    client_name = models.CharField('nombre cliente', max_length=100)
    commentary = models.CharField('comentario', max_length=200)
    url_perfil = models.URLField('url perfil', blank=True, null=True)
    url_photo = models.URLField('url foto', blank=True, null=True)

    class Meta:
        verbose_name = 'comentario cliente'
        verbose_name_plural = 'comentarios clientes'
        ordering = ['-created']

    def __str__(self):
        return self.client_name



@python_2_unicode_compatible
class ContactUs(TimeStampedModel):
    ESTRELLA_5 = '3'
    ESTRELLA_4 = '2'
    ESTRELLA_3 = '1'
    ECONOMY = '0'

    MODE_CHOICES = (
        (ESTRELLA_5, '5 star'),
        (ESTRELLA_4, '4 star'),
        (ESTRELLA_3, '3 star'),
        (ECONOMY, 'Economy'),
    )

    COMPARTIDO = '2'
    PRIVADO = '1'
    MODE_CHOICES_HOTEL = (
        (PRIVADO, 'privado'),
        (COMPARTIDO, 'compartido'),

    )
    name = models.CharField('nombre', max_length=50)
    last_name = models.CharField('apellido', max_length=150, blank=False, null=False)
    email = models.EmailField('correo', blank=False, null=False)
    phone = models.CharField('telefono', max_length=15)
    skype = models.URLField('skype', max_length=150)
    best_time_contact = models.CharField('Mejor momento para contactarlo', max_length=200)
    country_residence = models.CharField('pais de residencia', max_length=20)
    city = models.CharField('ciudad', max_length=15)
    destiny = models.ForeignKey(Destiny, on_delete=models.CASCADE)
    departure_date = models.DateField('fecha de salida')
    days_amount = models.IntegerField('cantidad de dias')
    adult_amount = models.IntegerField('cantidad de adultos')
    infant_amount = models.IntegerField('cantidad de infantes')
    boy_infant_amount = models.IntegerField('cantidad de niños menosres de 2 a 3')
    boy_amount = models.IntegerField('cantidad de niños mayores a 3 años')
    hotel = models.CharField(
        'hotel',
        max_length=2,
        blank=True,
        choices=MODE_CHOICES
    )
    type_service = models.CharField(
        'tipo de servicio',
        max_length=2,
        blank=True,
        choices=MODE_CHOICES_HOTEL
    )
    message = models.TextField('mensaje')








