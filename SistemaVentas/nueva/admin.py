from django.contrib import admin
from .models import *

admin.site.register(Empresas)

# @ vamos a usar un decorador 

@admin.register(Orden)
class OrdenAdmin(admin.ModelAdmin):
    list_display = ('codigo_orden', 'fecha_orden', 'cliente', 'empleado','estados','iva','total')
    list_filter = ('fecha_orden',)

    def get_readonly_fields(self, request, obj = None):
        if obj:
            return [ 'cliente', 'empleado']
        return []
@admin.register(Marca)
class MarcaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)
    
@admin.register(Detalle_orden)
class Detalle_ordenAdmin(admin.ModelAdmin):
    list_display = ('orden','producto','cantidad','subtotal')
    def get_readonly_fields(self, request, obj = None):
        if obj:
            return ['orden', 'cantidad','subtotal']
        return []
    
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
    
@admin.register(MetodoPago)
class MetodoPagoAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)

# Register your models here.
