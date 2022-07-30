from tkinter import N
from django.shortcuts import render
from django.http import HttpResponse
from datetime import date, datetime
from mi_app.models import Curso, Estudiante, Profesor
from mi_app.forms import CursoFormulario, CursoBusquedaFormulario, ProfesorFormulario, EstudianteFormulario
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView, View
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from mi_app.forms import userRegisterForm, userLoginForm
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required

# --------- Sector de la pagina web. --------- #


def mostrar_index(request):
    return render(request, "mi_app/index.html", {"mi_titulo": "Bienvenido, suscribase para recibir notificaciones sobre lo ultimo en reseñas de los nuevos lanzamientos."})


# --------- Sector de las listas de las diferentes clases de los models. --------- #


def listar_cursos(request): # vista
    context = {}
    context["cursos"] = Curso.objects.all() # modelo
    return render(request, "mi_app/lista_cursos.html", context) # template


def listar_estudiantes(request):
    context = {}
    context["estudiantes"] = Estudiante.objects.all()
    return render(request, "mi_app/lista_estudiantes.html", context)

def listar_profesores(request):
    context = {}
    context["profesores"] = Profesor.objects.all()
    return render(request, "mi_app/lista_profesores.html", context)


# --------- Sector de las formularios. --------- #


def formulario_curso(request):

    if request.method == "POST":
        
        mi_formulario = CursoFormulario(request.POST)

        print(mi_formulario)

        if  mi_formulario.is_valid():

            datos = mi_formulario.cleaned_data 

            curso = Curso(nombre=datos["curso"], camada=datos["camada"])

            curso.save()

            return render(request, "mi_app/gracias.html", {"mensaje":"agregado con exito!"})
   
    else:

        mi_formulario = CursoFormulario()
    
    return render(request, "mi_app/curso_formulario.html", {"mi_formulario":mi_formulario})


def profesor_formulario(request):

    if request.method == "POST":
        
        mi_formulario_profesor = ProfesorFormulario(request.POST)

        print(mi_formulario_profesor)

        if  mi_formulario_profesor.is_valid():

            data = mi_formulario_profesor.cleaned_data 

            profe = Profesor(nombre=data["nombre"], apellido=data["apellido"], email=data["email"], profesion=data["profesion"],)

            profe.save()

            return render(request, "mi_app/gracias.html")
   
    else:

        mi_formulario_profesor = ProfesorFormulario()
    
    return render(request, "mi_app/Profesor_Formulario.html", {"mi_formulario_profesor":mi_formulario_profesor})




def estudiante_formulario(request):

    if request.method == "POST":
        
        mi_formulario_estudiante = EstudianteFormulario(request.POST)

        print(mi_formulario_estudiante)

        if  mi_formulario_estudiante.is_valid():

            dato = mi_formulario_estudiante.cleaned_data 

            alumno = Estudiante(Nombre=dato["Nombre"], Apellido=dato["Apellido"], Email=dato["Email"],)

            alumno.save()

            return render(request, "mi_app/gracias.html")
   
    else:

        mi_formulario_estudiante = EstudianteFormulario()
    
    return render(request, "mi_app/Estudiante_formulario.html", {"mi_formulario_estudiante":mi_formulario_estudiante})



# --------- Sector de las busquedas de formularios. --------- #

def formulario_busqueda(request):

    busqueda_formulario = CursoBusquedaFormulario()

    if request.GET:    
        busqueda_formulario = CursoBusquedaFormulario(request.GET)
        if busqueda_formulario.is_valid():
            criterio = busqueda_formulario.cleaned_data
            cursos = Curso.objects.filter(nombre = criterio['criterio']).all()
            #cursos = Curso.objects.filter(nombre=busqueda_formulario.cleaned_data.get("criterio")).all()
            return render(request, "mi_app/curso_busqueda.html", {"cursos": cursos})

#"busqueda_formulario": busqueda_formulario
    return render(request, "mi_app/curso_busqueda.html", {"busqueda_formulario": busqueda_formulario})



def contacto(request):

    if request.method == "POST":
        
        return render(request, "mi_app/gracias.html")

    return render(request,"mi_app/contacto.html")


def busqueda_productos(request):

    return render(request, "mi_app/busqueda_productos.html")



def mostrar_signup(request):

    return render(request, "mi_app/Panel_signup.html")


def mostrar_about_us(request):

    return render(request, "mi_app/SobreNosotros.html")


def eliminarProfesor(request,profesor_nombre):

    profesor = Profesor.objects.get(nombre=profesor_nombre)
    profesor.delete()

    profesores = Profesor.objects.all()

    contexto = {"profesores":profesores}

    return render(request, "mi_app/lista_profesores.html", contexto)










# login - signup - logout 
# templates: Panel_Signup.html - user_form.html(registro) - login.html - panel_logout.html
class usuarioRegistro(SuccessMessageMixin, CreateView):
    success_message = 'Usuario creado satisfactoriamente!'
    template_name = 'mi_app/user_form.html'
    success_url = reverse_lazy('login')
    form_class = userRegisterForm
    

def usuario_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contraseña = form.cleaned_data.get('password')
            user = authenticate(username = usuario, password = contraseña) # si existen los datos en la bd
            if user is not None:
                login(request, user)
                return render(request, 'mi_app/index.html', {'mensaje' : f'Hola {usuario}! '})
            else:
                return render(request, 'mi_app/index.html', {'mensaje' : ''})
        else:
            return render(request, 'mi_app/index.html', {'mensaje' : 'Contraseña o nombre de usuario mal ingresados.' })
    form = AuthenticationForm()
    return render(request, 'mi_app/login.html', {'form' : form })

    
class PanelLogout(LogoutView):
    template_name = 'mi_app/panel_logout.html'




    

