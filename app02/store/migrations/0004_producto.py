# Generated by Django 3.1.2 on 2020-10-24 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20201022_1717'),
    ]

    operations = [
        migrations.CreateModel(
            name='producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Nombre del producto')),
                ('price', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Precio')),
                ('stock', models.PositiveIntegerField(verbose_name='stock')),
                ('description', models.CharField(max_length=300, verbose_name='Descripcion del producto')),
            ],
        ),
    ]