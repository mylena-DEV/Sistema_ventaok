from django.contrib import admin
from .models import *



@admin.register(Factura)
class FacturaAdmin(admin.ModelAdmin):
    list_display = ('subtotal','iva','total')


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('stock',)
    
@admin.register(Compras)
class ComprasAdmin(admin.ModelAdmin):
    list_display = ('total',)


