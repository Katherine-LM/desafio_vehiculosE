from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Vehiculo, Chofer, RegistroContable

def crear_vehiculo(request):
    matricula = request.GET.get('matricula')
    marca = request.GET.get('marca')
    modelo = request.GET.get('modelo')
    año = request.GET.get('año')
    vehiculo = Vehiculo.objects.create(matricula=matricula, marca=marca, modelo=modelo, año=año)
    return JsonResponse({'status': 'Vehículo creado', 'vehiculo_id': vehiculo.id})

def crear_chofer(request):
    nombre = request.GET.get('nombre')
    licencia = request.GET.get('licencia')
    chofer = Chofer.objects.create(nombre=nombre, licencia=licencia)
    return JsonResponse({'status': 'Chofer creado', 'chofer_id': chofer.id})

def crear_registro_contable(request):
    vehiculo_id = request.GET.get('vehiculo_id')
    detalles = request.GET.get('detalles')
    vehiculo = get_object_or_404(Vehiculo, id=vehiculo_id)
    registro = RegistroContable.objects.create(vehiculo=vehiculo, detalles=detalles)
    return JsonResponse({'status': 'Registro contable creado', 'registro_id': registro.id})

def deshabilitar_chofer(request, chofer_id):
    chofer = get_object_or_404(Chofer, id=chofer_id)
    chofer.habilitado = False
    chofer.save()
    return JsonResponse({'status': 'Chofer deshabilitado'})

def deshabilitar_vehiculo(request, vehiculo_id):
    vehiculo = get_object_or_404(Vehiculo, id=vehiculo_id)
    vehiculo.habilitado = False
    vehiculo.save()
    return JsonResponse({'status': 'Vehículo deshabilitado'})

def habilitar_chofer(request, chofer_id):
    chofer = get_object_or_404(Chofer, id=chofer_id)
    chofer.habilitado = True
    chofer.save()
    return JsonResponse({'status': 'Chofer habilitado'})

def habilitar_vehiculo(request, vehiculo_id):
    vehiculo = get_object_or_404(Vehiculo, id=vehiculo_id)
    vehiculo.habilitado = True
    vehiculo.save()
    return JsonResponse({'status': 'Vehículo habilitado'})

def obtener_vehiculo(request, vehiculo_id):
    vehiculo = get_object_or_404(Vehiculo, id=vehiculo_id)
    return JsonResponse({
        'matricula': vehiculo.matricula,
        'marca': vehiculo.marca,
        'modelo': vehiculo.modelo,
        'año': vehiculo.año,
        'habilitado': vehiculo.habilitado,
        'chofer': vehiculo.chofer.nombre if vehiculo.chofer else None
    })

def obtener_chofer(request, chofer_id):
    chofer = get_object_or_404(Chofer, id=chofer_id)
    return JsonResponse({
        'nombre': chofer.nombre,
        'licencia': chofer.licencia,
        'habilitado': chofer.habilitado
    })

def asignar_chofer_a_vehiculo(request, vehiculo_id, chofer_id):
    vehiculo = get_object_or_404(Vehiculo, id=vehiculo_id)
    chofer = get_object_or_404(Chofer, id=chofer_id)
    vehiculo.chofer = chofer
    vehiculo.save()
    return JsonResponse({'status': 'Chofer asignado al vehículo'})

def imprimir_datos_vehiculos(request):
    vehiculos = Vehiculo.objects.all()
    datos = [{
        'matricula': v.matricula,
        'marca': v.marca,
        'modelo': v.modelo,
        'año': v.año,
        'habilitado': v.habilitado,
        'chofer': v.chofer.nombre if v.chofer else None
    } for v in vehiculos]
    return JsonResponse({'vehiculos': datos})
