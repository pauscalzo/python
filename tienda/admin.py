from django.contrib import admin

# Register your models here.

from .models import Producto, Categoria, Marca

admin.site.register(Producto)
admin.site.register(Categoria)
admin.site.register(Marca)

