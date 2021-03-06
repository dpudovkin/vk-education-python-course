# Generated by Django 3.2.9 on 2021-11-15 12:57

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('orders', '0002_auto_20211113_1610'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('clients', '0004_rename_user_id_client_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='home_address',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='orders.address',
                                    verbose_name='Домашний адрес'),
        ),
        migrations.AlterField(
            model_name='client',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL,
                                       to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]
