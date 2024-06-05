from django.urls import path
from .views import (
    crear_vehiculo,
    crear_chofer,
    crear_registro_contable,
    deshabilitar_chofer,
    deshabilitar_vehiculo,
    habilitar_chofer,
    habilitar_vehiculo,
    obtener_vehiculo,
    obtener_chofer,
    asignar_chofer_a_vehiculo,
    imprimir_datos_vehiculos
)

urlpatterns = [
    path('crear_vehiculo/', crear_vehiculo),
    path('crear_chofer/', crear_chofer),
    path('crear_registro_contable/', crear_registro_contable),
    path('deshabilitar_chofer/<int:chofer_id>/', deshabilitar_chofer),
    path('deshabilitar_vehiculo/<int:vehiculo_id>/', deshabilitar_vehiculo),
    path('habilitar_chofer/<int:chofer_id>/', habilitar_chofer),
    path('habilitar_vehiculo/<int:vehiculo_id>/', habilitar_vehiculo),
    path('obtener_vehiculo/<int:vehiculo_id>/', obtener_vehiculo),
    path('obtener_chofer/<int:chofer_id>/', obtener_chofer),
    path('asignar_chofer_a_vehiculo/<int:vehiculo_id>/<int:chofer_id>/', asignar_chofer_a_vehiculo),
    path('imprimir_datos_vehiculos/', imprimir_datos_vehiculos),
]
