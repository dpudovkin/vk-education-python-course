from django.db import models


class User(models.Model):
    name = models.CharField(max_length=20, verbose_name='Имя')
    full_name = models.CharField(max_length=50, verbose_name='Полное имя (ФИО)')
    birth_day = models.DateField(verbose_name='День рождение', null=True)
    phone_number = models.CharField(max_length=11, null=False, verbose_name='Номер телефона')


