from django.db import models
from django.contrib.auth.models import User 

# Create your models here.

class Medicamento(models.Model):
    nombreMarca = models.CharField(max_length=30)
    drogaComponente = models.CharField(max_length=30)
    laboratorio = models.CharField(max_length=30)
    codigoBarra = models.IntegerField() 

class Laboratorio(models.Model):
    nombreLab = models.CharField(max_length=30)
    direccionLab = models.CharField(max_length=50)
    telefonoLab = models.IntegerField()

class Accion(models.Model):
    nombreAccion = models.CharField(max_length=30)
    descripcionAccion = models.CharField(max_length=80) 

class Sucursal(models.Model):
    nombreSucursal = models.CharField(max_length=40)
    direccionSucursal = models.CharField(max_length=50)
    municipioSucursal = models.CharField(max_length=30)
    ciudadSucursal = models.CharField(max_length=30)
    telefonoSucursal = models.IntegerField()

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    image = models.ImageField(upload_to="avatares", null=True, blank=True)
