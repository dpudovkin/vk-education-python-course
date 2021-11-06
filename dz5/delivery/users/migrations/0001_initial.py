# Generated by Django 3.2.9 on 2021-11-06 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Имя')),
                ('full_name', models.CharField(max_length=50, verbose_name='Полное имя (ФИО)')),
                ('birth_day', models.DateField(null=True, verbose_name='День рождение')),
                ('phone_number', models.CharField(max_length=11, verbose_name='Номер телефона')),
            ],
        ),
    ]