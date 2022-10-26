from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms

class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ("username", "password")

class RegistrarForm(UserCreationForm):
    first_name = forms.CharField(label='Nombres:', strip=False)
    last_name = forms.CharField(label='Apellidos:', strip=False)
    email = forms.EmailField(label='Correo:')
    username = forms.CharField(label= 'Nombre de usuario:', strip=False)
    password1 = forms.CharField(label= 'contraseña:', strip=False, widget=forms.PasswordInput)
    password2 = forms.CharField(label= 'repite contraseña:', strip=False, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "username", "password1", "password2")