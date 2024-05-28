
from django.contrib import admin
from django.urls import path, include
from perro import views
from refugio import views
from django.views.generic.base import RedirectView
from django.shortcuts import redirect


urlpatterns = [
    path('admin/', admin.site.urls),
    path('refugio/', include('refugio.urls')),
    path('perro/', include('perro.urls')),
    path('', lambda request: redirect('refugio/home', permanent=True)),
    path('/', lambda request: redirect('refugio/home', permanent=True)),
    path('', lambda request: redirect('perro/home', permanent=True)),
    path('/', lambda request: redirect('perro/home', permanent=True)),


]
    



    #path('', views.home, name='home'),
    #path('signup/', views.signup, name='signup'),
    #path('refugio/', views.listar_perros, name='refugio'),
    #path('logout/', views.cerrar_sesion, name='cerrar_sesion'),
    #path('signin/', views.inicioSesion, name='signin'),
    #path('agregar/', views.agregarPerro, name='AgregarPerro'),
    #path('refugio/<int:perro_id>/', views.perro_detail, name='perro_detail'),
    #path('refugio/<int:perro_id>/delete', views.perro_delete, name='perro_delete'),

