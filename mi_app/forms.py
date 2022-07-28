from django import forms


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