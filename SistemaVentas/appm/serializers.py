#Los serializadores convierten los registros en formato json(clave valor, ejmeplo : 'usuario':'Carlos')
from rest_framework import serializers
from .models import Clientes, Productos


class ClientesSerializer(serializers.ModelSerializer):
    class Meta: #debemos indicar los metadatos con los que va a trabajr el serializador
        model= Clientes #Llamamos al modelo de vamos a utilizar 
        fields = ['cedula','nombre','apellido','telefono','email','direccion','fecha_creacion','fecha_nacimiento']#debemos indicar los campos que van a ser parte del serializador
