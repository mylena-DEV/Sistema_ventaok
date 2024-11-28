from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError


class Producto(models.Model):
    numero = models.IntegerField()
    nombre = models.CharField(max_length=50)
    stock = models.IntegerField(validators= [MinValueValidator(1)])
    precio = models.FloatField()

    
    def restar_stock(self, cantidad):
            self.stock = self.stock - cantidad
            self.save()

  
    def sumar_stock(self,cantidad):
        self.stock = self.stock + cantidad
        self.save()

class Factura(models.Model):
    codigo = models.CharField(max_length=10)
    producto = models.ForeignKey(Producto,on_delete=models.CASCADE)
    cantidad = models.IntegerField(validators=[MinValueValidator(1)])
    subtotal = models.FloatField(default=0.00,null=True,blank=True,editable=False)
    iva = models.FloatField(default=0.00,null=True,blank=True,editable=False)
    total = models.FloatField(default=0.00,null=True,blank=True,editable=False)

    def clean(self):
        if self.cantidad > self.producto.stock:
            raise ValidationError('no debe exceder al stock')

   
    def save(self, *args, **kwargs):
        self.producto.restar_stock(self.cantidad)
        self.subtotal = self.cantidad * self.producto.precio
        self.iva = self.subtotal * 0.15
        self.total = self.iva + self.subtotal
        self.clean()
        super().save(*args, **kwargs)
        
class Compras(models.Model):
    numero_compras = models.IntegerField()
    producto = models.ForeignKey(Producto,on_delete=models.CASCADE)
    #subtotal = models.FloatField(default=0.00,null=True,blank=True,editable=False)
    cantidad = models.IntegerField()
    total = models.FloatField(default=0.00,null=True,blank=True,editable=False)
    def save(self, *args, **kwargs):
        self.total = self.cantidad * self.producto.precio
        self.producto.sumar_stock(self.cantidad)
        super().save(*args, **kwargs)
    
    