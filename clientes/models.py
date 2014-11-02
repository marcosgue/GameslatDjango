from django.db import models

from phonenumber_field.modelfields import PhoneNumberField


class Cliente(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    DNI_CUIT = models.CharField(max_length=11, unique=True)
    email = models.EmailField(blank=True)
    phone = PhoneNumberField()
    address = models.CharField(max_length=70, blank=True)
    city = models.CharField(max_length=25, blank=True)
    state = models.CharField(max_length=25, blank=True)
    postal_code = models.CharField(max_length=8, blank=True)
    points = models.PositiveIntegerField()
    es_favorito = models.BooleanField(default=False)
