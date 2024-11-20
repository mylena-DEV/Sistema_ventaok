from django.db import models
from .choices import CATEGORIAS
from django.core.validators import MinValueValidator, MaxValueValidator, MaxLengthValidator, MinLengthValidator

class Clientes(models.Model):
    cedula = models.CharField(max_length=10,primary_key=True, unique=True, validators= [MinLengthValidator(10)])
    apellido = models.CharField(max_length=50, blank=False, verbose_name='Apellido del cliente: ')
    nombre = models.CharField(max_length=50,blank=False, verbose_name='Nombre del cliente: ')
    direccion = models.CharField(max_length=100, blank=False, verbose_name='Dirección del cliente: ')
    telefono = models.CharField(max_length=10, blank=False, verbose_name='Telefono del cliente: ')
    email = models.CharField(max_length=50, blank=False, verbose_name= 'Ingresar email: ')
    Fecha_nacimiento = models.DateField(blank=False,verbose_name='Fecha de nacimiento: ')
    
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"
# lo utilizamos en singular cuando llama al modelo
# en los metadatos al momento que hace el llamado en singular 
#el verbos name plural al momento de llamar al cliente para 

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        db_table = 'Clientes'
        
class Productos(models.Model):
    codigo = models.CharField(max_length=10, primary_key=True, unique=True)
    nombre = models.CharField(max_length=50, blank=False, verbose_name='Nombre del producto: ')
    precio = models.DecimalField(max_digits=10, decimal_places=2, blank=False, help_text='ingresa valores con decimal',verbose_name='Precio del producto: ')
    fecha_ingreso = models.DateTimeField(auto_now_add=True)
    fecha_elaboracion = models.DateField()
    fecha_vencimento = models.DateField()
    cantidad_stock = models.IntegerField(verbose_name='Cantidad en stock' ) 
    marca = models.CharField(max_length=50,unique=True, blank=False, verbose_name='Marca')
    caractersiticas_categoria = models.CharField(max_length=100, choices=CATEGORIAS)
    
    #creamos una funcion para actualizar el stock 
    #pasamos como parametro la cantidad y guanrdando los cambios con save
    #actualzar stock para 
    def actualizar_stock(self, cantidad):
        self.cantidad_stock -= cantidad
        self.save()
    # simplificar la operacion / -= es una forma de operar (parecido a los contadores )siempre y cuando sea una sola operacion
    # choice listar en una forma de dupla una serie de elemnetos (registros limitados puedo crear un choices)
    def __str__(self):
        return f"{self.nombre} {self.marca}"
    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        db_table = 'Productos'
    