from django.db import models

# Create your models here.
class cliente(models.Model):
    firstname = models.CharField(max_length=80, verbose_name='Nombre')
    lastname = models.CharField(max_length=80, verbose_name='Apellidos(s)')
    phone = models.CharField(max_length=20, verbose_name='Telefono')
    email = models.CharField(max_length=100, verbose_name='Email')
    direction = models.CharField(max_length=100, verbose_name='direccion')

    def __str__(self):
        return self.firstname
class Meta:
            verbose_name= 'Cliente'
            verbose_name_plural= 'Clientes'


class proveedor(models.Model):
    firstname = models.CharField(max_length=80, verbose_name='Nombre')
    lastname = models.CharField(max_length=80, verbose_name='Apellidos(s)')
    phone = models.CharField(max_length=20, verbose_name='Telefono')
    email = models.CharField(max_length=100, verbose_name='Email')
    direction = models.CharField(max_length=100, verbose_name='direccion')

    def __str__(self):
        return "{0} {1} :: {2}".format(self.firstname, self.lastname, self.direction)
    class Meta:
        verbose_name= 'Proveedor'
        verbose_name_plural= 'Proveedores'


class producto(models.Model):
    name = models.CharField(max_length=200, verbose_name='Nombre del producto')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Precio')
    stock = models.PositiveIntegerField(verbose_name='stock')
    description = models.CharField(max_length=300, verbose_name='Descripcion del producto')

    def __str__(self):
        return "{0}".format(self.name)
    class Meta:

            verbose_name= 'Producto'
            verbose_name_plural= 'Productos'