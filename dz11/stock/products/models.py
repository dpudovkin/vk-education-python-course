from django.db import models


class EventModel(models.Model):
    name = ""

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.pk:
            pass
            # res = send_model_created_report.delay(f"Created model:\n Model class:
            # {self.__class__} \n Model name: {self.name}")
        super(EventModel, self).save(*args, **kwargs)


class Product(EventModel):
    name = models.CharField(null=False, max_length=256, verbose_name='Наименование товара')
    description = models.TextField(null=False, default="description", verbose_name='Описание товара', max_length=2500)
    origin_country = models.CharField(null=True, verbose_name='Страна происхождения', max_length=128)
    brand = models.ForeignKey(to='products.Brand', null=True, on_delete=models.SET_NULL, verbose_name='Бренд продукта')
    category = models.ForeignKey(to='Category', null=True, on_delete=models.SET_NULL, verbose_name='Категория продукта')

    def __str__(self):
        return self.name


class Brand(EventModel):
    name = models.CharField(null=False, max_length=256, verbose_name='Наименвоание бренда')
    is_premium = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Category(EventModel):
    name = models.CharField(null=False, max_length=256, verbose_name='Наименование категории')
    displayed = models.BooleanField(default=True)

    def __str__(self):
        return self.name
