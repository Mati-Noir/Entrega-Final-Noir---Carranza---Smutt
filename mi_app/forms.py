from dataclasses import fields
from doctest import master
from tkinter import Widget
from django import forms
from django.contrib.auth.models import User
from .models import Post
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm



# ---- Sector formularios del usuario y su perfil ---- #


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


        
class EditProfileForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_login = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    is_superuser = forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
    is_staff = forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
    is_active = forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
    #date_joined = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'last_login', 'is_superuser', 'is_staff', 'is_active')


# ---- Sector formularios de las reseñas ---- #


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','title_tag','author','body', 'image')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Algun titulo para colocar'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control','placeholder':'Nombre de la pestaña al entrar al articulo'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control','placeholder':'Escriba lo que desee sobre el articulo. Acuerdese de usar "<p>" al inicio y "<p/>" al final para hacer parrafos. En caso de querer resaltar utilize "<strong>" y "<strong/>" para destacar en negrita alguna frase/palabra. '}),
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','title_tag','body', 'image')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Algun titulo para colocar'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control','placeholder':'Nombre de la pestaña al entrar al articulo'}),
            #'author': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control','placeholder':'Escriba lo que desee sobre el articulo. Acuerdese de usar "<p>" al inicio y "<p/>" al final para hacer parrafos. En caso de querer resaltar utilize "<strong>" y "<strong/>" para destacar en negrita alguna frase/palabra. '}),
        }
