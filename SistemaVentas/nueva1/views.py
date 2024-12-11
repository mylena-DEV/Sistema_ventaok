from django.core.exceptions import ValidationError
#mensaje de confirmacion atravez de un numero
from django.core.validators import RegexValidator #para hacer validaciones especiales letras y espacio (o expresiones regulares)
def validacion_numeros(value):
    if not value.isdigit():
        raise ValidationError("El valor debe contener solo números") #raise funciona como como un print para devolver un mensajhe en caso de que no se cumpla la condicion
    
def Validacion_letras(value):
    if not value.isalpha():
        raise ValidationError("El valor debe contener solo letras")

 #expresiones regulares
   
validacion_especial = RegexValidator(
    regex= r'^[a-zA-Z\s]+$', #para establecer la expresion regular o cadena permitidos 
    message= 'el campo solo debe contener letras y espacios'

)

#validacion numeros letras y espacios
validacion_especial2 = RegexValidator(
    regex= r'^[a-zA-Z0-9\s]+$', #para establecer la expresion regular o cadena permitidos 
    message= 'el campo solo debe contener letras y espacios'

)

#validacion numeros, letras y espacios y caracteres espcailes
validacion_especial3 = RegexValidator(
    regex= r'^[a-zA-Z0-9,-ó\s]+$', #para establecer la expresion regular o cadena permitidos 
    message= 'el campo solo debe contener letras y espacios'
)

from .serializers import ClientesSerializer, ProductosSerializer, OrdenSerializer, EmpresasSerializer, EmpleadosSerializer, ProveedoresSerializer, Detalle_ordenSerializer
from rest_framework import viewsets
from .models import Clientes, Productos, Orden , Empresas, Empleados, Proveedores, Detalle_orden

#vistas sirve para acceder a los metodos que ofrece una api (metodo post/get/delete/put)
#post : para enviar informacion especificamente en los formularios
#get : para enviar/obtener informacion
#put: para actualizar informacion
#delete: para borrar informacion
#(parametros)
#clas es la plantilla (en base ala clase se crea el objeto)el modelo contiene la clase y la clase obtiene el objeto

class ClientesViewSet(viewsets.ModelViewSet):
    queryset = Clientes.objects.all() #sirve para traer todos los objetos del modelo clientes
    serializer_class = ClientesSerializer #sirve para indicar cual es el serializador que va a utilizar la vista

class ProductosViewSet(viewsets.ModelViewSet):
    queryset = Productos.objects.all()
    serializer_class =  ProductosSerializer

class OrdenViewSet(viewsets.ModelViewSet):
    queryset = Orden.objects.all()
    serializer_class =  OrdenSerializer

class EmpresasViewSet(viewsets.ModelViewSet):
    queryset = Empresas.objects.all()
    serializer_class = EmpresasSerializer   

class EmpleadosViewSet(viewsets.ModelViewSet):
    queryset = Empleados.objects.all()
    serializer_class = EmpleadosSerializer
    
class ProveedoresViewSet(viewsets.ModelViewSet):
    queryset = Proveedores.objects.all()
    serializer_class = ProveedoresSerializer
    
class Detalle_ordenViewSet(viewsets.ModelViewSet):
    queryset = Detalle_orden.objects.all()
    serializer_class = Detalle_ordenSerializer


