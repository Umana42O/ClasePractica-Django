from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('agregar', agregar, name='agregar'),
    path('eliminar/<str:name>', eliminar, name='eliminar'),
    path('<str:name>', descripcion, name='descripcion'),
    
]
