from django.contrib import admin
from .models import Usuarios, Roles, Documento, Registro

# Register your models here.
admin.site.register(Usuarios)
admin.site.register(Roles)
admin.site.register(Documento)
admin.site.register(Registro)