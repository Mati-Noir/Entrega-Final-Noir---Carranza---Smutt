from tkinter import N
from django.shortcuts import render
from django.http import HttpResponse
from datetime import date, datetime
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView, View, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from mi_app.forms import userRegisterForm
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostForm , EditForm, EditProfileForm
from django.views import generic

# --------- Sector de la pagina web. --------- #


def mostrar_index(request):
    return render(request, "mi_app/index.html", {"mi_titulo": "Bienvenido a Practac Gaming News. Visite nuestro sector de reseñas para enterarse de los ultimos lanzamientos mas esperados del año."})


def mostrar_signup(request):

    return render(request, "mi_app/Panel_signup.html")


# --------- Sector de About us + terms + P.P. --------- #

def mostrar_terms(request):

    return render(request, "mi_app/Terms.html")

def mostrar_politicas_privacidad(request):

    return render(request, "mi_app/Politicas_de_Privacidad.html")

def mostrar_about_us(request):

    return render(request, "mi_app/SobreNosotros.html")





# ---- Sector Login - Signup - Logout ---- #

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

# ------- Sector de panel de reseñas -------- #
    

class Lista_Reseñas(ListView):
    model = Post
    template_name = 'post_list.html'
    ordering = ['-post_date']
    #ordering = ['-id']

# ------- CRUD de las reseñas/articulos -------- #

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'mi_app/article-detail.html'


class AddPostView(LoginRequiredMixin ,CreateView):
    model = Post
    form_class = PostForm
    template_name = 'mi_app/add_post.html'
    #fields = '__all__'
    success_url = reverse_lazy('Post_list')

class UpdatePostView(LoginRequiredMixin ,UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'mi_app/update_post.html'
    #fields = ['title', 'title_tag', 'body']

class DeletePostView(LoginRequiredMixin , DeleteView):
    model = Post
    template_name = 'mi_app/delete_post.html'
    success_url = reverse_lazy('Post_list')
    
    
# ------- CRUD de las reseñas/articulos -------- #

class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'mi_app/edit_profile.html'
    success_url = reverse_lazy('Post_list')

    def get_object(self):
        return self.request.user
    

# ------- Cambio de contraseña -------- #

class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    #success_url: reverse_lazy('Post_list')
    success_url = reverse_lazy('password_success')

def password_success(request):
    return render(request, 'mi_app/password_success.html', {})
