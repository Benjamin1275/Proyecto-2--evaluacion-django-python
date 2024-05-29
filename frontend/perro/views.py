from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
   return render(request, 'home.html')

from django.template import loader

def base(request):
   template = loader.get_template('base.html')
   return HttpResponse(template.render())


def login(request):
   template = loader.get_template('signup.html')
   return HttpResponse(template.render())   
def register(request):
   template = loader.get_template('signin.html')
   return HttpResponse(template.render())    

  
def agregar_perro(request):
   template = loader.get_template('agregar_perro.html')
   return HttpResponse(template.render()) 

def perro_details(request):
   template = loader.get_template('perro_details.html')
   return HttpResponse(template.render())              