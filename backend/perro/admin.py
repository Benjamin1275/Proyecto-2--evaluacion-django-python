from django.contrib import admin
from .models import Region, Provincia, Comuna, Perro

admin.site.register(Region)
admin.site.register(Provincia)
admin.site.register(Comuna)
admin.site.register(Perro)


class RefugioAdmin(admin.ModelAdmin):
    readonly_fields = ('fecha_registro',)




