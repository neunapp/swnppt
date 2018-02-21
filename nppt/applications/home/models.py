
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
#app blog
from applications.blog.models import Blog
#applications servicio
from applications.servicio.models import Service



@python_2_unicode_compatible
class Home(TimeStampedModel):

    title_seo = models.CharField('titulo seo', max_length=200)
    description_seo = models.CharField('descripcion seo', max_length=200)
    title_seo = models.CharField('titulo seo redes sociales', max_length=200)
    description_seo = models.CharField('descripcion seo redes sociales', max_length=200)
    title = models.CharField('titulo banner', max_length=200, blank=True)
    slogan = models.CharField('slogan banner', max_length=200, blank=True)
    banner_img = models.ImageField('imagen de banner 1', upload_to='home', blank=True, null=True)
    banner_img2 = models.ImageField('imagen de banner 2', upload_to='home', blank=True, null=True)
    banner_img3 = models.ImageField('imagen de banner 3', upload_to='home', blank=True, null=True)
    banner_img4 = models.ImageField('imagen de banner 4', upload_to='home', blank=True, null=True)
    title_featured_article = models.CharField(
        'titulo articulo destacado',
        max_length=200,
        blank=True
    )
    featured_article = models.ForeignKey(
        Blog,
        on_delete=models.CASCADE,
        related_name='home_articulo_destcado',
        verbose_name='articulo destacado',
        null=True,
        blank=True,
    )
    title_featured_service = models.CharField(
        'titulo servicio mas solicitado',
        max_length=200,
        blank=True
    )
    featured_service = models.ForeignKey(
        Service,
        on_delete=models.CASCADE,
        related_name='home_servicio_destcado',
        verbose_name='servicio destacado',
        null=True,
        blank=True,
    )
    title_emblema_article = models.CharField('titulo articulo emblema', max_length=200)
    emblema_article = models.ForeignKey(
        Blog,
        on_delete=models.CASCADE,
        related_name='home_articulo_emblema',
        verbose_name='articulo emblema',
        null=True,
        blank=True,
    )
    title_content1_article = models.CharField('titulo contenido 1', max_length=200)
    content1_article = models.ForeignKey(
        Blog,
        on_delete=models.CASCADE,
        related_name='home_contenido_1',
        verbose_name='contenido 1',
        null=True,
        blank=True,
    )
    title_content2_article = models.CharField('titulo contenido 2', max_length=200)
    content2_article = models.ForeignKey(
        Blog,
        on_delete=models.CASCADE,
        related_name='home_contenido_2',
        verbose_name='contenido 2',
        null=True,
        blank=True,
    )
    phone1 = models.CharField('WhatsApp', max_length=60, blank=True)
    email = models.EmailField('E-mail', blank=True)
    link_face = models.URLField('Facebook', blank=True, null=True)
    link_instagram = models.URLField('instragram', blank=True, null=True)
    link_youtube = models.URLField('youtube', blank=True, null=True)
    link_tripadvisor = models.URLField('tripadvisor', blank=True, null=True)
    title_feature_enterprice = models.CharField(
        'titulo caracteristica empresa',
        max_length=200,
        blank=True
    )
    values_enterprice = models.ManyToManyField(
        Blog,
        verbose_name='valores de la empresa',
        blank=True
    )

    class Meta:
        verbose_name = 'Pagina Pricipal'
        verbose_name_plural = 'Pagina Principal'
        ordering = ['-created']

    def __str__(self):
        return self.title


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
    skype = models.CharField('ID en Skype', blank=True, max_length=100)
    best_time_contact = models.CharField('Mejor momento para contactarlo', max_length=200)
    country_residence = models.CharField('pais de residencia', max_length=20)
    city = models.CharField('ciudad', max_length=15)
    destiny = models.ManyToManyField(Destiny)
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

    class Meta:
        verbose_name = 'Formulario de Contacto'
        verbose_name_plural = 'Formulario de Contactos'
        ordering = ['-created']

    def __str__(self):
        return self.client_name
