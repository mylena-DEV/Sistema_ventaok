from django.contrib import admin
from .models import *

admin.site.register(Empresas)

# @ vamos a usar un decorador 

@admin.register(Orden)
class OrdenAdmin(admin.ModelAdmin):
    list_display = ('codigo_orden', 'fecha_orden', 'cliente', 'empleado')
    list_filter = ('fecha_orden',)

@admin.register(Detalle_orden)
class Detalle_OrdenAdmin(admin.ModelAdmin):
    list_display = ('orden', 'estados', 'producto', 'cantidad','subtotal', 'iva', 'total')
    
@admin.register(Clientes)
class ClientesAdmin(admin.ModelAdmin):
    list_display = ('cedula', 'nombre', 'apellido', 'direccion', 'telefono', 'email')
    list_filter = ('cedula', 'apellido')
    search_fields = ('cedula', 'nombre', 'apellido')

@admin.register(Empleados)
class EmpleadosAdmin(admin.ModelAdmin):
    list_display = ('cedula', 'nombre', 'apellido', 'direccion', 'telefono', 'email')
    list_filter = ('cedula', 'apellido')
    search_fields = ('cedula', 'nombre', 'apellido')
    
@admin.register(Productos)
class ProductosAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre', 'precio', 'cantidad_stock', 'fecha_ingreso', 'fecha_elaboracion', 'fecha_vencimiento')
    list_filter = ('fecha_ingreso', 'fecha_elaboracion', 'fecha_vencimiento')
    search_fields = ('codigo', 'nombre', 'descripcion')
    
@admin.register(Proveedores)
class ProveedoresAdmin(admin.ModelAdmin):
    list_display = ('cedula', 'nombre', 'apellido', 'telefono', 'email')
    list_filter = ('cedula', 'apellido')
    search_fields = ('cedula', 'nombre', 'apellido')
    

# Register your models here.
