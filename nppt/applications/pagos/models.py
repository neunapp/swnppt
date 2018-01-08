#third party

from model_utils.models import TimeStampedModel

#django libraries

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

#model from another app

from applications.servicio.models import Service


@python_2_unicode_compatible
class Discount_offert(TimeStampedModel):

    name = models.CharField('nombre oferta', max_length=50)
    offert_code = models.CharField('codigo promocion', max_length=20)
    description = models.CharField('descripcion', max_length=200)
    date_limit = models.DateTimeField('fecha limite')
    use_number = models.IntegerField('numero de usuario')

    class Meta:
        verbose_name = 'descuento'
        verbose_name_plural = 'descuentos'
        ordering = ['-created']

    def __str__(self):
        return self.name


class Client(TimeStampedModel):

    user = models.CharField('usuario', max_length=150)
    skype = models.CharField('skype', max_length=150)
    country = models.CharField('pais', max_length=25)
    city = models.CharField('ciudad', max_length=25)

    class Meta:
        verbose_name = 'cliente'
        verbose_name_plural = 'clientes'
        ordering = ['-created']

    def __str__(self):
        return self.user


class Sale(TimeStampedModel):

    date_sale = models.DateTimeField()
    client = models.ForeignKey(Client, related_name='cliente', on_delete=models.CASCADE)
    state = models.BooleanField('estado')

    class Meta:
        verbose_name = 'venta'
        verbose_name_plural = 'ventas'
        ordering = ['-created']

    def __str__(self):
        return self.date_sale


class Detail_sale(TimeStampedModel):

    service = models.ForeignKey(Service, related_name='servicio', on_delete=models.CASCADE)
    sale = models.ForeignKey(Sale, related_name='venta', on_delete=models.CASCADE)
    sale_price = models.CharField('precio venta', max_length=50)
    amount = models.DecimalField('cantidad', max_digits=5, decimal_places=2)
    discount = models.ForeignKey(Discount_offert, related_name='descuento', on_delete=models.CASCADE)
    igv = models.DecimalField('IGV', max_digits=5, decimal_places=2)

    class Meta:
        verbose_name = 'servicio'
        verbose_name_plural = 'servicios'
        ordering = ['-created']

    def __str__(self):
        return self.service