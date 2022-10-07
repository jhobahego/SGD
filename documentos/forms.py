from socket import fromshare
from tkinter import Widget
from django import forms
from .models import Usuarios

class RolesForm(forms.ModelForm):
    class Meta:
        model = Usuarios
        Widget = {
            'contra': forms.PasswordInput(),
        }