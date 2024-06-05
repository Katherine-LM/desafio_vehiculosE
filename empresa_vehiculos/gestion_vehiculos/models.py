from django.db import models

class Chofer(models.Model):
    nombre = models.CharField(max_length=100)
    licencia = models.CharField(max_length=100, unique=True)
    habilitado = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

class Vehiculo(models.Model):
    matricula = models.CharField(max_length=100, unique=True)
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    año = models.IntegerField()
    habilitado = models.BooleanField(default=True)
    chofer = models.ForeignKey(Chofer, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'{self.marca} {self.modelo} ({self.matricula})'

class RegistroContable(models.Model):
    vehiculo = models.OneToOneField(Vehiculo, on_delete=models.CASCADE)
    detalles = models.TextField()

    def __str__(self):
        return f'Registro contable del vehículo {self.vehiculo.matricula}'
