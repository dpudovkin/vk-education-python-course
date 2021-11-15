from django.db import models

from users.models import User


class Employee(models.Model):
    job = models.CharField(max_length=30, null=False, verbose_name='Должность сотрудника')
    status = models.CharField(max_length=30, null=False, verbose_name='Статус сотрудника')
    user = models.OneToOneField(to=User, null=True, verbose_name='Пользователь',
                                on_delete=models.SET_NULL)

    def __str__(self):
        if self.user is None:
            return f"Employee id: {self.id} {self.job}"
        if self.user.full_name is None:
            return f"{str(self.user.username)} {self.job}"
        return f"{str(self.user.full_name)} {self.job}"
