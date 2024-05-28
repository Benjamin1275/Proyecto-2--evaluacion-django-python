#from django.contrib import admin
from django.urls import path
from . import views_backend
from . import views_restfull
#from . import views_soap #Poner comentario
from . import views_load
from rest_framework_simplejwt import views as jwt_views
urlpatterns = [
    # path('hijo_ventas/', admin.site.urls),
    #path('indexharrys/', views_backend.indexHarrys),
    path('load/', views_load.LoadData.as_view()),

    path('backend/region/',  views_backend.RegionList.as_view()),
    path('backend/provincia/<int:region>',  views_backend.ProvinciaList.as_view()),
    path('backend/comuna/<int:provincia>',  views_backend.ComunaList.as_view()),
    path('backend/perro/', views_backend.PerroList.as_view()),
    path('backend/perro/<int:pk>', views_backend.PerroDetail.as_view()),

    #path('backend/login/', views_backend.ClienteDetail.as_view()),
    path('API/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    #curl -d "username=harrys&password=macarena" -X POST http://localhost:9010/ventas/api/token/
    path('API/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    #curl -d "refresh=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYyMzQ0NjEzNiwianRpIjoiMjcyOTI0OTkwOGVhNGQ2ZjkxMDFiMGI4ZjhlZDZkY2QiLCJ1c2VyX2lkIjoyfQ.zkCWbKBnkDCukZVB8cHiCnrUOHRl1vWF6Oqg29IFT7A" -X POST http://localhost:9010/ventas/api/token/refresh/ {"access":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjIzMzY1NDU3LCJqdGkiOiJlZjljNWFiYjI1MzU0YWJjYjc4YWRmNTI2MDA2OTEwNCIsInVzZXJfaWQiOjJ9.RPrfobpIF52W0wdNJk4zLYcgWpymZdgAPFxOIH0KEsk"}

    #  BackEnd Oficial


    #  RestFull
    path('restfull/region/', views_restfull.rf_region),  
    path('restfull/region/<int:cod_region>', views_restfull.rf_region_pk),

    path('restfull/region_load', views_restfull.rf_load_region),


    #path('soap_service/', views_soap.my_soap_application), # Poner comentario
    #path('soap_service_harrys/', views_soap.pruebaHarrys), # Poner comentario
    #path('soap_service_persona/', views_soap.crud_persona), # Poner comentario
    


    

    #path('soap_service_consumir/', views_soap.SoapList.as_view()),

]
