from django.contrib import admin
from django.urls import path, include
from refugio import views
from perro import views


urlpatterns = [
    path('home', views.home, name='post_list'),
    path('base', views.base, name='post_list'),
    path('login', views.login, name='post_list'),
    path('register', views.register, name='post_list'),
    path('agregar_perro', views.agregar_perro, name='post_list'),
    path('perro_details', views.perro_details, name='post_list'),
]
