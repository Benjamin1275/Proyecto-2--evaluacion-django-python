from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
   return render(request, 'home.html')

from django.template import loader

def base(request):
   template = loader.get_template('base.html')
   return HttpResponse(template.render())


#def login(request):
#   template = loader.get_template('signup.html')
#   return HttpResponse(template.render())   
#def register(request):
#   template = loader.get_template('signin.html')
#   return HttpResponse(template.render())    

  
def info_refugio(request):
   template = loader.get_template('info_refugio.html')
   return HttpResponse(template.render()) 

