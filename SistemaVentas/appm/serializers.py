#Los serializadores convierten los registros en formato json(clave valor, ejmeplo : 'usuario':'Carlos')
from rest_framework import serializers
from .models import Clientes, Productos, Empresas, Factura, Proveedores, Empleados
#listas en corchetes , parametros llaves
class ClientesSerializer(serializers.ModelSerializer):
    class Meta: #debemos indicar los metadatos con los que va a trabajar el serializador
        model= Clientes #Llamamos al modelo de vamos a utilizar 
        fields = ['cedula','nombre','apellido','telefono','email','direccion','fecha_creacion','fecha_nacimiento']#debemos indicar los campos que van a ser parte del serializador
class ProductosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Productos
        fields = ['codigo', 'nombre','caracteristicas_categoria', 'marca' , 'precio', 'cantidad_stock', 'fecha_ingreso', 'fecha_elaboracion', 'fecha_vencimiento']
class EmpresasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresas 
        fields = ['ruc', 'nombre', 'direccion', 'telefono', 'email']

class FacturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Factura
        fields = ['codigo_factura', 'fecha_factura', 'cliente', 'empleado', 'producto', 'cantidad','subtotal', 'iva', 'total']

class ProveedoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedores
        fields = ['cedula', 'nombre', 'apellido', 'telefono', 'email', 'direccion', 'fecha_creacion', 'fecha_nacimiento']

class EmpleadosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleados
        fields = ['cedula', 'nombre', 'apellido', 'direccion', 'telefono', 'email', 'fecha_creacion', 'fecha_nacimiento']








#funcion tiene que tener parametros (todas las clases tienen parametros)
#modulo : modelo (el que se crea)
#Los viewsets proveen una manera de organizar y gestionar los endpoints de una API RESTful