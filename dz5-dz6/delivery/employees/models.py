from django.db import models

from users.models import User


class Employee(models.Model):
    job = models.CharField(max_length=30, null=False, verbose_name='Должность сотрудника')
    status = models.CharField(max_length=30, null=False, verbose_name='Статус сотрудника')
    user_id = models.OneToOneField(to=User, null=False, verbose_name='Пользователь',
                                   on_delete=models.PROTECT)
