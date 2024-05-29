from django.contrib import admin
from django.urls import path, include
from refugio import views as refugio_views
from perro import views as perro_views

urlpatterns = [
    path('home', refugio_views.home, name='home'),
    path('base', refugio_views.base, name='base'),
    path('login', perro_views.login, name='login'),
    path('register', perro_views.register, name='register'),
    path('agregar_perro', perro_views.agregar_perro, name='agregar_perro'),
    path('perro_details', perro_views.perro_details, name='perro_details'),
]