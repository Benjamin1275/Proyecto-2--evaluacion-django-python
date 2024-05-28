from django.contrib import admin
from django.urls import path, include
#from perro import views as perro_views
#from refugio import views as refugio_views


urlpatterns = [
    path('admin/', admin.site.urls),
    #path('refugio/', include('refugio.urls')),
    #path('perro/', include('perro.urls')),


]