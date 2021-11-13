from django.db import models

from users.models import User


class Client(models.Model):
    status = models.CharField(null=False, default='NOT VERIFIED', max_length=20,
                              verbose_name='Статус клиента')
    home_address = models.ForeignKey(to='orders.Address', null=True, on_delete=models.PROTECT,
                                     verbose_name='Домашний адрес')
    user_id = models.OneToOneField(to=User, null=False, verbose_name='Пользователь',
                                   on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.user_id.full_name} {self.status}"
