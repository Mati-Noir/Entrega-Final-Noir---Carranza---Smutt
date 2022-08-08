from django.contrib import admin
from django.urls import path
from mi_app.views import mostrar_index, mostrar_about_us, usuarioRegistro, PanelLogout, usuario_login
from mi_app import views
from .views import ArticleDetailView, Lista_Reseñas, AddPostView, UpdatePostView, DeletePostView


urlpatterns = [
    path('', mostrar_index),
    path('mi-pagina/', mostrar_index, name = 'pagina-inicial'),
    path('Sobre_Nosotros/',views.mostrar_about_us,name="mostrar_about_us"),
    path('registro/', usuarioRegistro.as_view(), name = 'usuario-registro'),
    path('panel-logout/', PanelLogout.as_view(), name = 'Panel-Logout'),
    path('login/', views.usuario_login , name = 'login'), # login momentaneo hasta que funcione el del bootstrap
    path('Terminos/',views.mostrar_terms,name="mostrar_terms"),
    path('Politica_Privacidad/',views.mostrar_politicas_privacidad,name="mostrar_politicas_privacidad"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),
    path('Post_list/', Lista_Reseñas.as_view(), name='Post_list'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('article/edit/<int:pk>',UpdatePostView.as_view(), name='update_post'),
    path('article/<int:pk>/remove',DeletePostView.as_view(), name='delete_post'),
]



