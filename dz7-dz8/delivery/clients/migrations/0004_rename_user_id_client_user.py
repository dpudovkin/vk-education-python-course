# Generated by Django 3.2.9 on 2021-11-13 16:10

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('clients', '0003_client_user_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='user_id',
            new_name='user',
        ),
    ]
