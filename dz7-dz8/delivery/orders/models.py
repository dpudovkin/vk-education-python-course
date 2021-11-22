from django.db import models

from clients.models import Client
from employees.models import Employee


class Address(models.Model):
    full_name = models.CharField(max_length=255, verbose_name='Наименование адреса')
    longitude = models.FloatField(null=False, verbose_name='Долгота')
    latitude = models.FloatField(null=False, verbose_name='Ширина')

    def __str__(self):
        return self.full_name


class OrderManager(models.Manager):

    def connected_with_user(self, user_id, order_id=None):
        clients = Client.objects.filter(user_id=user_id)
        employees = Employee.objects.filter(user_id=user_id)
        result = self.none()
        for client in clients:
            result = result | self.filter(arriving_client_id=client.id).all()
            result = result | self.filter(destination_client_id=client.id).all()

        for employee in employees:
            result = result | self.filter(performer_id=employee.id).all()

        if order_id is not None:
            result = result & self.filter(id=order_id).all()

        return result



class Order(models.Model):
    objects = OrderManager()

    destination_client = models.ForeignKey(to=Client, null=True, on_delete=models.SET_NULL,
                                           related_name='received_orders',
                                           verbose_name='Клиент получающий отправление')
    arriving_client = models.ForeignKey(to=Client, null=True, on_delete=models.SET_NULL,
                                        related_name='sent_orders',
                                        verbose_name='Клиент отдающий отправление')
    destination_address = models.ForeignKey(to=Address, on_delete=models.SET_NULL,
                                            related_name='received_orders',
                                            verbose_name='Адрес назначения заказа', null=True)
    arriving_address = models.ForeignKey(to=Address, on_delete=models.SET_NULL,
                                         related_name='sent_orders',
                                         verbose_name='Адрес отправления заказа', null=True)
    cost = models.IntegerField(default=0, verbose_name='Стоимость заказа для клиента')
    comment = models.CharField(max_length=255, verbose_name='Дополнительный комментарий к заказу', default='')
    status = models.CharField(max_length=20, verbose_name='Статус заказа', default='NEW')
    base_award = models.IntegerField(verbose_name='Базовое вознаграждение курьеру за выполненный заказ', default=0)
    performer = models.ForeignKey(to=Employee, null=True, on_delete=models.SET_NULL,
                                  verbose_name='Курьер')

    def __str__(self):
        return f"Order #{self.id} {self.status}"
