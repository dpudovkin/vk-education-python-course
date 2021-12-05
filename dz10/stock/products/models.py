from django.db import models

from tracker.tasks import send_model_created_report, backup_product_list


class EventModel(models.Model):
    name = ""

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.pk:
            res = send_model_created_report.delay(f"Created model:\n Model class: {self.__class__} \n Model name: {self.name}")
        super(EventModel, self).save(*args, **kwargs)


class Product(EventModel):
    name = models.CharField(null=False, max_length=256, verbose_name='Наименование товара')
    brand = models.ForeignKey(to='products.Brand', null=True, on_delete=models.SET_NULL, verbose_name='Бренд продукта')
    category = models.ForeignKey(to='Category', null=True, on_delete=models.SET_NULL, verbose_name='Категория продукта')

    def __str__(self):
        return self.name


class Brand(EventModel):
    name = models.CharField(null=False, max_length=256, verbose_name='Наименвоание бренда')

    def __str__(self):
        return self.name


class Category(EventModel):
    name = models.CharField(null=False, max_length=256, verbose_name='Наименование категории')

    def __str__(self):
        return self.name
