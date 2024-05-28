from django.contrib import admin
from .models import Region, Provincia, Comuna, Perro


class PerroAdmin(admin.ModelAdmin):
    readonly_fields = ('fecha_registro',)
    
admin.site.register(Perro, PerroAdmin)
admin.site.register(Region)
admin.site.register(Provincia)
admin.site.register(Comuna)








