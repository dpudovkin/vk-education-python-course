from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    full_name = models.CharField(max_length=50, verbose_name='Полное имя (ФИО)', null=True)
    birth_day = models.DateField(verbose_name='Дата рождения', null=True)
    phone_number = models.CharField(max_length=11, null=False, verbose_name='Номер телефона')
    avatar = models.ImageField(upload_to='avatars', null=False, default='user.png', verbose_name='Аватарка пользователя')

    def __str__(self):
        return self.full_name