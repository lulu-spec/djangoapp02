# Generated by Django 3.1.2 on 2020-10-22 22:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_proveedor'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='proveedor',
            options={'verbose_name': 'Proveedor', 'verbose_name_plural': 'Proveedores'},
        ),
    ]