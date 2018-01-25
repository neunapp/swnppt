from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

#managers
from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):

    GENDER_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    )
    username = models.CharField(
        'usuario',
        max_length=100,
        unique=True
    )
    email = models.EmailField(
        'correo electronico',
        unique=True
    )
    first_name = models.CharField(
        'nombres',
        max_length=50,
        blank=True)
    last_name = models.CharField(
        'apellidos',
        max_length=50,
        blank=True)
    avatar = models.URLField(
        'foto',
        blank=True,
    )
    phone = models.CharField(
        'telefono',
        max_length=50,
        blank=True,
        null=True
    )
    gender = models.CharField(
        'sexo',
        max_length=1,
        choices=GENDER_CHOICES,
        blank=True,
        null=True
    )
    date_birth = models.DateField(
        'fecha de nacionmiento',
        blank=True,
        null=True
    )
    addresse = models.CharField(
        'direccion',
        blank=True,
        max_length=100
    )
    nacionality = models.CharField(
        'nacionalidad',
        max_length=60,
    )

    objects = UserManager()

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nacionality', ]

    def get_short_name(self):
        return self.email
