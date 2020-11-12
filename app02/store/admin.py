from django.contrib import admin
from .models import cliente, proveedor, producto
 

# Register your models here.


admin.site.register(cliente)
admin.site.register(proveedor)
admin.site.register(producto)