from rest_framework.views import APIView
from django.http import JsonResponse

class LoadMenu(APIView):
    def get(self, request, format=None):
        return JsonResponse({'BACKEND_Perro': 'http://localhost:9010/perro/backend/'
                            ,'API': 'http://localhost:9010/API/xx/'
                            ,'Administrador':'http://localhost:9010/admin'
                            ,'Load_Perro':'http://localhost:9010/perro/load/'
                            ,'BACKEND_Refugio': 'http://localhost:9010/refugio/backend/',
                            'Load_Refugio':'http://localhost:9010/refugio/load/'
                            })
    
