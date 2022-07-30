from doctest import master
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User



class CursoFormulario(forms.Form):

    curso = forms.CharField()
    camada = forms.IntegerField()


class CursoBusquedaFormulario(forms.Form):
    criterio = forms.CharField()

class EstudianteFormulario(forms.Form):
    Nombre= forms.CharField(max_length=40)
    Apellido= forms.CharField(max_length=40)
    Email= forms.EmailField()

class ProfesorFormulario(forms.Form):   
    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    email= forms.EmailField()
    profesion= forms.CharField(max_length=30)


class userRegisterForm(UserCreationForm):
    username = forms.CharField(max_length = 40)
    email = forms.EmailField()
    password1 = forms.CharField(label='Password', widget = forms.PasswordInput)
    password2 = forms.CharField(label='Repeat Password', widget = forms.PasswordInput)
    first_name = forms.CharField()
    last_name = forms.CharField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name']
        help_texts = {k:'' for k in fields}
