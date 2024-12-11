from django.contrib import admin
from django.urls import path , include #sirve para incluir las rutas dentro del servidor 
from nueva1.views import ClientesViewSet, ProductosViewSet, EmpleadosViewSet, EmpresasViewSet, ProveedoresViewSet, OrdenViewSet, Detalle_ordenViewSet
from rest_framework.routers import DefaultRouter #sirve para poder crear las rutas  permite crear un objeto para acceder al metodo register (para acceder a las url)

rutas = DefaultRouter()
rutas.register('clientes', ClientesViewSet)
rutas.register('productos', ProductosViewSet)
rutas.register('empleados', EmpleadosViewSet)
rutas.register('empresas', EmpresasViewSet)
rutas.register('proveedores', ProveedoresViewSet)
rutas.register('orden', OrdenViewSet)
rutas.register('Detalle_orden', Detalle_ordenViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(rutas.urls)),  # Rutas principales
]
