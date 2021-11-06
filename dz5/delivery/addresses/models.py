from django.db import models


class Address(models.Model):
    full_name = models.CharField(max_length=255, verbose_name='Наименование адреса')
    longitude = models.FloatField(null=False, verbose_name='Долгота')
    latitude = models.FloatField(null=False, verbose_name='Ширина')

