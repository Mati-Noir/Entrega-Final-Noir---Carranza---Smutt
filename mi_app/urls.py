from django.contrib import admin
from django.urls import path
from mi_app.views import (listar_profesores, 
         listar_cursos, listar_estudiantes, mostrar_index,
        formulario_curso,estudiante_formulario, mostrar_about_us,
        usuarioRegistro, PanelLogout, usuario_login
    )
from mi_app import views 


urlpatterns = [
    path('mi-pagina/', mostrar_index, name = 'pagina-inicial'),
    path('listar-cursos/', views.listar_cursos, name="listar-cursos"),
    path('listar-estudiantes/', views.listar_estudiantes, name="listar-estudiantes"),
    path('listar-profesores/', views.listar_profesores, name="listar-profesores"),
    path('formulario_curso/', views.formulario_curso, name="formulario_curso"),
    path('formulario_profesores/',views.profesor_formulario, name="profesor_formulario"),
    path('formulario_estudiante/',views.estudiante_formulario, name="estudiante_formulario"),
    path('contacto/', views.contacto),
    path('busqueda_productos/',views.busqueda_productos),
    path('buscar_curso/',views.formulario_busqueda, name="formulario_busqueda"),
    path('Sobre_Nosotros/',views.mostrar_about_us,name="mostrar_about_us"),
    path('registro/', usuarioRegistro.as_view(), name = 'usuario-registro'),
    path('panel-logout/', PanelLogout.as_view(), name = 'Panel-Logout'),
    path('login/', views.usuario_login , name = 'login'), # login momentaneo hasta que funcione el del bootstrap
    path('Terminos/',views.mostrar_terms,name="mostrar_terms"),
    path('Politica_Privacidad/',views.mostrar_politicas_privacidad,name="mostrar_politicas_privacidad"),
    
]



