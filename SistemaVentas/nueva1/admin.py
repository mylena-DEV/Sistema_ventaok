from django.contrib import admin
from .models import *
admin.site.register(Empresas)

# @ vamos a usar un decorador 

class Detalle_ordenInline(admin.TabularInline):
    model = Detalle_orden
    extra = 1  # Añade una fila extra para nuevos detalles
   
    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['orden', 'subtotal','producto','cantidad']
        return ['subtotal']
    

@admin.register(Orden)
class OrdenAdmin(admin.ModelAdmin):
    inlines = [Detalle_ordenInline]
    list_display = ('codigo_orden', 'fecha_orden', 'cliente', 'empleado','estados','iva','total')
    list_filter = ('fecha_orden',)

    def get_readonly_fields(self, request, obj = None):
        if obj:
            return [ 'cliente', 'empleado','subtotal_general','iva','total', 'metodo_pago']
        return ['subtotal_general','iva','total']

    
@admin.register(Detalle_orden)
class Detalle_ordenAdmin(admin.ModelAdmin):
    list_display = ('orden','producto','cantidad','subtotal')

    def get_readonly_fields(self, request, obj = None):
        if obj:
            return ['orden', 'cantidad','subtotal','producto']
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
    

