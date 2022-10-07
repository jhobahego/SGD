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
    tipo = models.CharField(max_length=40)
    cantidad = models.IntegerField()

class Registro(models.Model):
    usuario_id = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    documento_id = models.ForeignKey(Documento, on_delete=models.CASCADE)
    tipo_venta = models.CharField(max_length=40)