from email.policy import default
from django.db import models

# Create your models here.
class Usuarios(models.Model):
    dni = models.IntegerField()
    nombres = models.CharField(max_length=40)
    apellidos = models.CharField(max_length=40)
    correo = models.CharField(max_length=60)
    contra = models.CharField(max_length=40)
    telefono = models.CharField(max_length=15)

class Roles(models.Model):
    nombre_rol = models.CharField(max_length=40)
    usuario_id = models.OneToOneField(Usuarios, on_delete=models.CASCADE)

class Documento(models.Model):
    autor = models.CharField(max_length=40)
    titulo = models.CharField(max_length=40)
    descripcion = models.TextField(max_length=200)
    tipo = models.CharField(max_length=40)
    categoria = models.CharField(max_length=40)
    stock = models.IntegerField()
    precio = models.IntegerField()

class Registro(models.Model):
    usuario_id = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    documento_id = models.ForeignKey(Documento, on_delete=models.CASCADE)
    tipo_venta = models.CharField(max_length=40)
    cantidad = models.IntegerField()