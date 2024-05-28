from django.contrib import admin
from django.urls import path, include
from refugio import views
from perro import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #Faltaria agregar las urls de las aplicaciones de views
    #path('', views.home, name='home'),
    #path('signup/', views.signup, name='signup'),
    #path('refugio/', views.listar_perros, name='refugio'),
    #path('logout/', views.cerrar_sesion, name='cerrar_sesion'),
    #path('signin/', views.inicioSesion, name='signin'),
    #path('agregar/', views.agregarPerro, name='AgregarPerro'),
    #path('refugio/<int:perro_id>/', views.perro_detail, name='perro_detail'),
    #path('refugio/<int:perro_id>/delete', views.perro_delete, name='perro_delete'),
    
]
