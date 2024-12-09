from django.contrib import admin
from django.urls import path , include #sirve para incluir las rutas dentro del servidor 
from nueva.views import ClientesViewSet, ProductosViewSet, EmpleadosViewSet, EmpresasViewSet,MarcaViewSet, ProveedoresViewSet, OrdenViewSet, Detalle_ordenViewSet, MetodoPagoViewSet
from rest_framework.routers import DefaultRouter #sirve para poder crear las rutas  permite crear un objeto para acceder al metodo register (para acceder a las url)

rutas = DefaultRouter()
rutas.register('clientes', ClientesViewSet)
rutas.register('productos', ProductosViewSet)
rutas.register('empleados', EmpleadosViewSet)
rutas.register('empresas', EmpresasViewSet)
rutas.register('proveedores', ProveedoresViewSet)
rutas.register('orden', OrdenViewSet)
rutas.register('Detalle_orden', Detalle_ordenViewSet)
rutas.register('Marca',MarcaViewSet)
rutas.register('MetodoPago',MetodoPagoViewSet)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(rutas.urls)),  # Rutas principales
]
