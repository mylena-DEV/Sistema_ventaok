from django.db import models
from .choices import CATEGORIAS, ESTADOS, VENDIDA, ANULADA, OPCIONES_PAGO
from decimal import Decimal
from django.core.validators import MinValueValidator, MaxValueValidator, MaxLengthValidator, MinLengthValidator
from .validadores import validacion_numeros, Validacion_letras, validacion_especial, validacion_especial2, validacion_especial3
from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import timedelta, date 

class Clientes(models.Model):
    cedula = models.CharField(primary_key=True, max_length=10, unique=True, validators= [MinLengthValidator(10), validacion_numeros])
    nombre = models.CharField(max_length=50, blank=False, verbose_name= 'Nombre del cliente : ', validators=[validacion_especial])
    apellido = models.CharField(max_length=50, blank=False, validators= [Validacion_letras])
    telefono = models.CharField(max_length=10,validators= [MinLengthValidator(10), validacion_numeros])
    email = models.EmailField(unique=True)
    direccion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_nacimiento = models.DateField()
    
    def __str__(self):
        return f"{self.nombre} - {self.apellido} "
    class Meta:
        verbose_name = 'Ingresa los datos del Cliente :'
        verbose_name_plural = 'datos Clientes'
        db_table = 'Clientes'

    
class Empresas(models.Model):
    ruc = models.CharField(primary_key=True, max_length=13, unique=True,validators= [MinLengthValidator(13), MaxLengthValidator(13), validacion_numeros])
    nombre = models.CharField(max_length=50, blank=False, verbose_name='Nombre de la empresa : ',validators= [Validacion_letras])
    direccion = models.TextField()
    telefono = models.CharField(max_length=10,validators= [MinLengthValidator(10), validacion_numeros])
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.nombre} "
    class Meta:
        verbose_name = 'Empresa :'
        verbose_name_plural = 'Empresas'
        db_table = 'Empresas'


class Proveedores (models.Model):
    nombre = models.CharField(max_length=50, blank=False, verbose_name='Nombre del proveedor : ',validators= [Validacion_letras])
    cedula = models.CharField(primary_key=True, max_length=10, unique=True, validators= [MinLengthValidator(10), validacion_numeros])
    apellido = models.CharField(max_length=50, blank=False,validators= [Validacion_letras])
    telefono = models.CharField(max_length=10,validators= [MinLengthValidator(10), validacion_numeros])
    email = models.EmailField(unique=True)
    empresa = models.ForeignKey(Empresas, on_delete= models.CASCADE)
    def __str__(self):
        return f"{self.nombre}  {self.apellido} "
    class Meta:
        verbose_name = 'Proveedor '
        verbose_name_plural = 'Proveedores'
        db_table = 'Proveedores'

class Productos(models.Model):
    codigo = models.PositiveBigIntegerField(primary_key=True, max_length=10, unique=True)
    nombre = models.CharField(max_length=50, blank=False, verbose_name=' Nombre del producto :') 
    proveedor = models.ForeignKey(Proveedores, on_delete=models.CASCADE)
    
    caracteristicas_categoria = models.CharField(max_length=100, choices= CATEGORIAS)
    precio = models.DecimalField(max_digits=10, decimal_places=2, help_text='ingresa valores con decimales', verbose_name='Precio del producto : ')
    cantidad_stock = models.IntegerField(verbose_name='Cantidad en stock : ')
    fecha_ingreso = models.DateTimeField(auto_now_add=True)
    fecha_elaboracion = models.DateField()
    fecha_vencimiento = models.DateField()
    
    def clean(self):
        if (self.fecha_vencimiento > (self.fecha_elaboracion + timedelta(days=365*5))) or (self.fecha_vencimiento<= self.fecha_elaboracion):
         raise ValidationError('El producto no puede estar vencido ni puede ser menor a la fecha de elaboración')

    
    def actualizar_stock (self, cantidad):
        self.cantidad_stock -= cantidad # -= es una forma de operar (parecido a los contadores) siempre y cuadno sea una sola operacion contador = contador + 1
        self.save()
    def actualizar_stock2(self, cantidad):
        self.cantidad_stock += cantidad
        self.save()
    def __str__(self):
        return f"{self.nombre}  {self.marca} "
    class Meta:
        verbose_name = 'Producto :'
        verbose_name_plural = 'Productos'
        db_table = 'Productos'

class Empleados (models.Model):
    cedula = models.CharField(primary_key=True, max_length=10, unique=True, verbose_name= 'Cedula del Empleado :', validators= [MinLengthValidator(10),validacion_numeros])
    nombre = models.CharField(max_length=50, blank=False, verbose_name='Nombre del Empleado : ',validators= [Validacion_letras])
    apellido = models.CharField(max_length=50, blank=False,validators= [Validacion_letras])
    telefono = models.CharField(max_length=10,validators= [MinLengthValidator(10),validacion_numeros])
    email = models.EmailField(unique=True)
    direccion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_nacimiento = models.DateField()
    def __str__(self):
        return f"{self.nombre} - {self.apellido} "
    class Meta:
        verbose_name = 'Empleado :'
        verbose_name_plural = 'Empleados'
        db_table = 'Empleados'
        
class MetodoPago(models.Model):
    nombre = models.CharField(max_length=100,choices=OPCIONES_PAGO, verbose_name="Método de Pago")
    descripcion = models.TextField(blank=True, null=True, verbose_name="Descripción")
    
    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Método de Pago"
        verbose_name_plural = "Métodos de Pago"

class Orden(models.Model):
    codigo_orden = models.AutoField(primary_key=True,unique=True,blank=False, null=False)
    fecha_orden = models.DateTimeField(auto_now_add=True)
    cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    empleado = models.ForeignKey(Empleados, on_delete=models.CASCADE)
    metodo_pago = models.ForeignKey(MetodoPago, on_delete=models.SET_NULL, null=True, verbose_name="Método de Pago")
    estados = models.CharField(max_length=50,choices=ESTADOS,default=VENDIDA)
    subtotal_general = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    iva = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    
    def actualizar_totales(self):
        detalles = Detalle_orden.objects.filter(orden=self)
        self.subtotal_general = sum(detalle.subtotal for detalle in detalles)
        self.iva = self.subtotal_general * Decimal(0.15)
        self.total = self.subtotal_general + self.iva
        self.save()
        
    def save(self, *args,**kwargs): 
        if self.estados == ANULADA:
            #obtenemos los detalles de la orden 
            detalles = Detalle_orden.objects.filter(orden=self)
            #iteramos cada detalle de orden
            for detalle in detalles:
                #reabastecemos el stock al producto
                detalle.producto.actualizar_stock2(detalle.cantidad)
                #recalculamos los totales a 0 porque la orden queda anulada
            self.iva = Decimal(0.00)
            self.total = Decimal(0.00) 
        super().save(*args, **kwargs)
   


    def __str__(self):
        return f"{self.codigo_orden} "
    class Meta:
        verbose_name = 'Orden'
        verbose_name_plural = 'Orden'
        db_table = 'Orden'
        
class Detalle_orden(models.Model):
    orden = models.ForeignKey(Orden, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    producto = models.ForeignKey(Productos, on_delete=models.CASCADE)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, editable=True, default=0.00,blank=True)
    
    def clean(self):
        if self.cantidad > self.producto.cantidad_stock:
            raise ValidationError('no debe exceder al stock')
    
    def save(self, *args, **kwargs):
        """Sobrescribe el método save para calcular valores automáticamente."""
        self.subtotal = self.cantidad * self.producto.precio
        #establecemos una condicion para  comprobar si el detalle de orden existe o no aun
        #self.pk es la clave primaria del detalle de orden
        #si el detalle es nuevo restamos del stock
        if not self.pk: 
            self.producto.actualizar_stock(self.cantidad)
        #si el detalle es modificado restamos o sumamos del stock
        else:
            #restamos o sumamos el stock según la diferencia entre la cantidad actual y la anterior
            detalle_anterior = Detalle_orden.objects.get(pk=self.pk)
            diferencia = self.cantidad-detalle_anterior.cantidad
            #si la diferencia es positiva, se resta del stock
            if diferencia > 0: 
                self.producto.actualizar_stock(diferencia)  
            #si la diferencia es negativa, se suma del stock
            elif diferencia < 0:
                self.producto.actualizar_stock2(-diferencia) 	
        super().save(*args, **kwargs)
        self.orden.actualizar_totales()
    
    class Meta:
        managed = True
        verbose_name = 'Detalles de orden'
        verbose_name_plural = 'Detalles de orden'
        
        
        
        
        
        
        
        




#metodo clean : sirbe para hacer una validacion antes de que se guarde un registro
#validar (un nuevo atributo), (restarle al stock),(vendida,anulada),(en el save if),(ultima factura estado)
#levantar requerimientos de una tienda funcionales y no funcionales
#orden(que agrega en el sistema) guarda e imprime

#mejorar el sistema * documentacion - entrevistas
#si una cedula tiene repetida la cedula
#si se borra los datos
#si un cliente nunca compro
#ver si hace falta un modelo
#fecha: 11 de diciembre
#tipo informe y # la otra semana mierocles 04 traer los proyectos de la tesis 
"""objetivo
alcance
beneficiarios"""
#17 pre defensa 
# ultima semana de enero 13 enero

#vendida anulada

#validaciones-nuevas