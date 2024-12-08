from django.urls import path
from . import views

app_name='vehiculo'
urlpatterns = [
    path('add/',views.agregar_vehiculo, name='agregar_vehiculo'),
    path('list/', views.listar_vehiculo, name='listar_vehiculo'),
]