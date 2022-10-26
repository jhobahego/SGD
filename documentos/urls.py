from django.urls import path
from documentos import views

urlpatterns = [
    path("", views.Index, name="index"),
    path("login/", views.Login, name="login"),
    path("registrar/", views.Registrar, name="registrar"),
    path("cerrar_sesion/", views.Cerrar_sesion, name="cerrar-sesion"),
]