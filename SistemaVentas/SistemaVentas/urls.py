from django.contrib import admin
from django.urls import path , include #sirve para incluir las rutas dentro del servidor 
from appm.views import ClientesViewSet
from rest_framework.routers import DefaultRouter #sirve para poder crear las rutas 

rutas = DefaultRouter()
rutas.register('clientes', ClientesViewSet, basename='clientes')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(rutas.urls)),  # Rutas principales
]
