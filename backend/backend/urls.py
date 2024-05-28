from django.contrib import admin
from django.urls import path,include
from . import views
from .views_serializer import router
urlpatterns = [
    path('admin/', admin.site.urls),
    #path('harrys/', admin.site.urls),
    path('API/', include(router.urls)),
    path('perro/', include(router.urls)),
    path('refugio/', include(router.urls)),

    path('', views.LoadMenu.as_view()),
    #path('/', views.LoadMenu.as_view()),
]
